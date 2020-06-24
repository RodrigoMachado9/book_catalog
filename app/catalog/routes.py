# app/catalog/routes.py
from app.catalog import bp
from flask import render_template
from app.catalog.models import Book, Publication
from app import db


@bp.route('/')
def display_books():
    books = Book.query.all()
    return render_template("home.html", books=books)
