from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet name", validators=[InputRequired(message="Pet name can't be blank")])
    species = SelectField("Species", validators=[InputRequired(message="Species can't be blank")],choices= [('cat','Cat'),('dog','Dog'),('porc','Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=1,max=30)])
    notes = StringField("Notes", validators=[Optional()])
    

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available= BooleanField('Availability')