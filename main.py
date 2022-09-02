# ====== FLASK STANDART LIBRARY =============
from flask import Blueprint, session, render_template
from flask_login import login_required, current_user
# ===============DATA BASE===============
from .models import Users

main = Blueprint('main', __name__)


@main.route('/')
def home_page():
    return render_template("homepage.html")


@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)
