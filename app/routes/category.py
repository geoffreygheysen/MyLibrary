from flask import flash, redirect, render_template, request, url_for
from app import app
from app.models.db.category import Category
from app.models.forms.category_form import CategoryForm
from app.tools.session_scope import session_scope

# Lister tous les categories
@app.route('/categories', methods=['GET'])
def get_categories():
    with session_scope() as session:
        categories = session.query(Category).all()
        category_data = [(c.id, c.name) for c in categories]
    return render_template('category/categories.html', categories=category_data)

# Créer une nouvelle categorie
@app.route('/category/create', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        new_category = Category(name=form.name.data)
        with session_scope() as session:
            session.add(new_category)
        return redirect(url_for('get_categories'))
    return render_template('category/create_category.html', form=form)

# Mettre à jour une catégorie existante
@app.route('/category/update/<int:id>', methods=['GET', 'POST'])
def update_category(id):
    form = CategoryForm()
    with session_scope() as session:
        category = session.query(Category).get(id)
        if not category:
            return redirect(url_for('get_categories'))
        if request.method == 'POST' and form.validate_on_submit():
            category.name = form.name.data
            session.add(category)
            return redirect(url_for('get_categories'))
        form.name.data = category.name
    return render_template('category/update_category.html', form=form, category_id=id)

# Supprimer une catégorie
@app.route('/category/delete/<int:id>', methods=['POST'])
def delete_category(id):
    with session_scope() as session:
        category = session.query(Category).get(id)
        if category:
            session.delete(category)
        else:
            # Optionnel : gérer le cas où la catégorie n'existe pas
            flash("Catégorie non trouvée.", "warning")
    return redirect(url_for('get_categories'))