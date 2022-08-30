# =========== STANDART LIBRARY FLASK ============
from flask_migrate import Migrate
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    # CONFIG DB
    USER_DB = "postgres"
    PASS = "admin"
    URL_DB = "localhost"
    NAME_DB = "noteme_users"
    FULL_URL_DB = f"postgresql://{USER_DB}:{PASS}@{URL_DB}/{NAME_DB}"

    # ===================ASIGNACION BASE DE DATOS=============
    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "7aS8cMYKV-HGK2YJUuc"

    db.init_app(app)

    # ===== MIGRATE CONFIG ==========
    migrate = Migrate()
    migrate.init_app(app, db)

    # ======== LOGIN MANAGER CONFIG ========
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import Users

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # ========= ROUTES ====================
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    # BLUE PRINT FOR AUTH ROUTES
    app.register_blueprint(auth_blueprint)
    # BLUEPRINT FOR NON AUTH ROUTES
    app.register_blueprint(main_blueprint)

    return app
