from flask import Blueprint, request, jsonify
from .models import Book
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return {"message": "Welcome to the Book Catalogue API!"}

# CREATE
@main_bp.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    if not data or not all(k in data for k in ("title", "author", "year")):
        return jsonify({"error": "Missing required fields"}), 400

    book = Book(
        title=data["title"],
        author=data["author"],
        year=int(data["year"])
    )
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book added", "book": book.to_dict()}), 201

# READ ALL
@main_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])

# READ ONE
@main_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.to_dict())

# UPDATE
@main_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()
    if "title" in data:
        book.title = data["title"]
    if "author" in data:
        book.author = data["author"]
    if "year" in data:
        book.year = int(data["year"])

    db.session.commit()
    return jsonify({"message": "Book updated", "book": book.to_dict()})

# DELETE
@main_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})