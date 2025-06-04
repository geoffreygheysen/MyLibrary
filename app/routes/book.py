from flask import redirect, render_template, url_for
from app import app
from app.models.db.book import Book
from app.models.forms.book_form import BookForm
from app.tools.session_scope import session_scope

# Lister tous les livres
@app.route('/books', methods=['GET'])
def get_books():
    with session_scope() as session:
        books = session.query(Book).all()
    return render_template('book/books.html', books=books)

# Créer un nouveau livre
@app.route('/book/create', methods=['GET', 'POST'])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
                title=form.title.data,
                publication_date=form.publication_date.data,
                author_id=form.author.data
            )
        with session_scope() as session:
            session.add(new_book)
        return redirect(url_for('get_books'))
    return render_template('book/create_book.html', form=form)