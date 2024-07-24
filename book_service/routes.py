from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from .forms import BookForm
import os

main_bp = Blueprint('main', __name__)

# Lista książek do wyświetlenia
books = []

# Folder na przesyłane pliki
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        cover_file = form.cover.data

        if cover_file:
            filename = secure_filename(cover_file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            cover_file.save(filepath)

            books.append({'title': title, 'author': author, 'cover': filename})
            return redirect(url_for('main.index'))

    return render_template('index.html', form=form, books=books)