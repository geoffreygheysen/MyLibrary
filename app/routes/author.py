from flask import redirect, render_template, url_for
from app import app
from app.models.db.author import Author
from app.models.forms.author_form import AuthorForm
from app.tools.session_scope import session_scope

# Lister tous les auteurs
@app.route('/authors', methods=['GET'])
def get_authors():
    with session_scope() as session:
        authors = session.query(Author).all()
    return render_template('author/authors.html', authors=authors)

# Créer un nouvel auteur
@app.route('/author/create', methods=['GET', 'POST'])
def create_author():
    form = AuthorForm()
    if form.validate_on_submit():
        new_author = Author(
            name=form.name.data,
            country=form.country.data
        )
        with session_scope() as session:
            session.add(new_author)
        return redirect(url_for('get_authors'))
    return render_template('author/create_author.html', form=form)