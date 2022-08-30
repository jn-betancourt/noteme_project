from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_login import UserMixin

from . import db


class Users(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))

    def __str__(self):
        return f"ID: {self.id} - Nombre: {self.name} - Email: {self.email}"


class UsersForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    send = SubmitField('Send')
