# ====== FLASK STANDART LIBRARY =============
from flask import Blueprint, session, render_template, make_response
from flask_login import login_required, current_user
# ===============DATA BASE===============
from .models import Users

main = Blueprint('main', __name__)


# ======= GENERIC VIEW ==============
@main.route('/')
def home_page():
    return render_template("homepage.html")


# ======== VIEW FOR LOGGED USERS ===========
@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")
