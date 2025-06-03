from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired(), Length(min=5)])