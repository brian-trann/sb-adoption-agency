'''Adoption Agency application'''

from flask import Flask, render_template, redirect, request, flash, session
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm,EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()

@app.route('/')
def index_page():
    ''' Index View. Query for all pets in database'''
    pets = Pet.query.all()
    return render_template('index.html',pets=pets)

@app.route('/add', methods=["GET","POST"])
def add_pet():
    '''Add Pet form; on error, re-render template'''
    form = AddPetForm()
    if form.validate_on_submit():
        pet_form = {k:v for k,v in form.data.items() if k != "csrf_token"}
        pet = Pet(**pet_form)
        db.session.add(pet)
        db.session.commit()
        flash(f"You've added {pet.name}!")
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=["GET","POST"])
def view_pet(pet_id):
    '''View pet route. Renders an edit form. Re-render's if error '''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"You've updated {pet.name}!")
        return redirect(f'/')
    else:
        return render_template('view_pet.html',pet=pet,form=form)