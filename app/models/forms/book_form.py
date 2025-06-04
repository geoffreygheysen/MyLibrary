from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import ListWidget, CheckboxInput

class BookForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired(), Length(min=5)])
    publication_date = DateField('Date de publication', format='%Y-%m-%d', validators=[DataRequired()])
    author = StringField('Auteur', validators=[DataRequired(), Length(min=5)])

    # Champ pour les catégories (choix à définir dynamiquement dans la vue)
    categories = SelectMultipleField(
        'Catégories',
        coerce=int,  # si les IDs sont des entiers
        validators=[DataRequired()],
        option_widget=CheckboxInput(),  # optionnel si tu veux afficher des cases à cocher
        widget=ListWidget(prefix_label=False)
    )

    submit = SubmitField('Créer')