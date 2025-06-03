from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class AuthorForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired(), Length(min=5)])
    country = StringField('Pays', validators=[DataRequired(), Length(min=5)])
    books = StringField('Livre(s) associé(s)', validators=[DataRequired()])