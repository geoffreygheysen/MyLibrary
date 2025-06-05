from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AuthorForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired(), Length(min=2)])
    country = StringField('Pays', validators=[DataRequired(), Length(min=2)])
    
    submit = SubmitField('Créer')