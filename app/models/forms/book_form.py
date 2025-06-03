from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired(), Length(min=5)])
    publication_date = DateField('Date de publication', format='%Y-%m-%d', validators=[DataRequired()])
    author = StringField('Auteur', validators=[DataRequired(), Length(min=5)])