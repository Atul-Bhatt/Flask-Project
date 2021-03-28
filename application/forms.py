from flask_wtf import FlaskForms
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForms):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegisterForm(FlaskForms):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    password_confirm = StringField(
        "Confirm Password", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register Now")
