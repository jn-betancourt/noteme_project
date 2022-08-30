# ====== FLASK STANDART LIBRARY =============
from flask import Blueprint, session, render_template
from flask_login import login_required, current_user
# ===============DATA BASE===============
from .models import Users

main = Blueprint('main', __name__)


@main.route('/')
def home_page():
    users = Users.query.all()
    lenght = Users.query.count()
    return render_template("homepage.html", users=users, lenght=lenght)


@main.route('/profile')
@login_required
def profile():
    return render_template("homepage.html", name=current_user.name)
