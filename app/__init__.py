# ========= MONGO DB IMPORT ==================
from .mongo_conexion import mongo_conexion

# =========== STANDART LIBRARY FLASK ============
from flask_migrate import Migrate
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# ======= INITIALIZED SQLalchemy =================
db = SQLAlchemy()

# ========== CONFIG MONGO DB =================
URI_MONGO_DB = "mongodb://localhost:27017/"
db_mongo = mongo_conexion(URI_MONGO_DB)


def create_app(setting_module):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(setting_module)

    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)

    # ===== MIGRATE CONFIG ==========
    migrate = Migrate()
    migrate.init_app(app, db)

    # ======== LOGIN MANAGER CONFIG ========
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    from .models import Users

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(str(user_id))

    # ========= ROUTES ====================
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    # ==== BLUE PRINT FOR AUTH ROUTES ======
    app.register_blueprint(auth_blueprint)
    # ====== BLUEPRINT FOR NON AUTH ROUTES ========
    app.register_blueprint(main_blueprint)

    return app
