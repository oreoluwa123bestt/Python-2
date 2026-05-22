# Book Catalogue API

A RESTful API built with Flask for managing book records through structured CRUD operations. This project demonstrates backend development concepts such as API routing, request handling, modular architecture, and database interaction.

---

## Features

- Create new book records
- Retrieve all books or a specific book
- Update existing book information
- Delete book records
- Structured Flask backend architecture
- Modular route handling

---

## Tech Stack

- Python
- Flask
- SQLite / SQLAlchemy *(change this if you used another database)*
- REST API principles

---

## Project Structure

```bash
book-catalogue-api/
│
├── app.py
├── config.py
├── models.py
├── routes.py
├── requirements.txt
└── README.md

```bash
# Clone and navigate
cd book-catalogue-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create instance folder
mkdir instance

# Run the app
python run.py
