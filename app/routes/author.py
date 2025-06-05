from flask import flash, redirect, render_template, request, url_for
from app import app
from app.models.db.author import Author
from app.models.forms.author_form import AuthorForm
from app.tools.session_scope import session_scope

# Lister tous les auteurs
@app.route('/authors', methods=['GET'])
def get_authors():
    with session_scope() as session:
        authors = session.query(Author).all()
        author_data = [(a.id, a.name, a.country, a.books) for a in authors]
    return render_template('author/authors.html', authors=author_data)

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

# Mettre à jour un auteur existant
@app.route('/author/update/<int:id>', methods=['GET', 'POST'])
def update_author(id):
    form = AuthorForm()
    with session_scope() as session:
        author = session.query(Author).get(id)
        if not author:
            return redirect(url_for('get_authors'))
        if request.method == 'POST' and form.validate_on_submit():
            author.name = form.name.data
            author.country = form.country.data
            session.add(author)
            return redirect(url_for('get_authors'))
        form.name.data = author.name
        form.country.data = author.country
    return render_template('author/update_author.html', form=form, author_id=id)

# Supprimer un auteur
@app.route('/author/delete/<int:id>', methods=['POST'])
def delete_author(id):
    with session_scope() as session:
        author = session.query(Author).get(id)
        if author:
            session.delete(author)
        else:
            # Optionnel : gérer le cas où la catégorie n'existe pas
            flash("Auteur non trouvée.", "warning")
    return redirect(url_for('get_authors'))