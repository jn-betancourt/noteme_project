# ======= STANDART LIBRARY FLASK =============
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
# ======= WERKZEUG SECURITY ==================
from werkzeug.security import generate_password_hash, check_password_hash
# ============ CLASSMODELS =========
from .models import UsersForm, Users

from . import db

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=["POST", "GET"])
def signup():
    user = Users()
    form = UsersForm(obj=user)
    if request.method == 'POST':
        if Users.query.filter_by(email=form.email.data).first():
            flash('Este usuario ya fue registrado')
            return redirect(url_for('auth.signup'))
        else:
            new_user = user.objects.create(email=form.email.data,
                                           name=form.name.data,
                                           last_name=form.last_name.data,
                                           password=generate_password_hash(form.password.data, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("main.profile"))

    return render_template("register.html", form=form)


@auth.route('/login', methods=["POST", "GET"])
def login():
    form = UsersForm()
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email=email).first()

    if request.method == "POST":
        if not user or not check_password_hash(user.password, password):
            flash("email o contraseña incorrectos")
            return redirect(url_for("auth.login"))
        else:
            login_user(user, remember=remember)
            return redirect(url_for("main.profile"))

    return render_template("login.html", form=form)


@auth.route('/logout', methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home_page"))
