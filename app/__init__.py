from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # === FIXED: Use absolute path for database ===
    base_dir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(base_dir, '..', 'instance')
    os.makedirs(instance_dir, exist_ok=True)
    
    db_path = f"sqlite:///{instance_dir}/books.db"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    print(f" Database connected successfully!")
    print(f" Database location: {db_path}")
    print("Book Catalogue API is running at http://127.0.0.1:5000")
    return app