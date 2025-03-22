from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, FileField, TextAreaField, RadioField, DateField, FileField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed
from datetime import datetime

class BlogPostForm(FlaskForm):
    title = StringField('Naslov', validators=[DataRequired(), Length(min=5, max=100)])
    content = TextAreaField('Sadržaj', render_kw={"id": "markdown-editor"})
    author = StringField('Autor', validators=[DataRequired()])
    status = RadioField('Status', choices=[('draft', 'Skica'), ('published', 'Objavljeno')], default='draft')
    date = DateField('Datum', default=datetime.today)
    tags = StringField('Oznake', render_kw={"id": "tags"})
    image = FileField('Blog Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Samo slike!')])
    submit = SubmitField('Spremi')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Zaporka', validators=[DataRequired()])
    remember_me = BooleanField('Ostani prijavljen')
    submit = SubmitField('Prijava')

class RegisterForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(3, 64), Email()])
    password = PasswordField('Zaporka', validators=[DataRequired(), Length(3, 30), EqualTo('password2', message='Zaporke moraju biti jednake.')])
    password2 = PasswordField('Potvrdi zaporku', validators=[DataRequired(), Length(3, 30)])
    submit = SubmitField('Registracija')

class ProfileForm(FlaskForm):
    first_name = StringField("Ime", validators=[DataRequired(), Length(max=50)])
    last_name = StringField("Prezime", validators=[DataRequired(), Length(max=50)])
    bio = TextAreaField("Biografija", validators=[Length(max=1000)], render_kw={"id": "markdown-editor"})
    submit = SubmitField("Spremi")
    theme = SelectField('Tema', choices=[
        ('', ''),
        ('cerulean', 'Cerulean'),
        ('cosmo', 'Cosmo'),
        ('cyborg', 'Cyborg'),
        ('darkly', 'Darkly'),
        ('flatly', 'Flatly'),
        ('journal', 'Journal'),
        ('litera', 'Litera'),
        ('lumen', 'Lumen'),
        ('lux', 'Lux'),
        ('materia', 'Materia'),
        ('minty', 'Minty'),
        ('morph', 'Morph'),
        ('pulse', 'Pulse'),
        ('quartz', 'Quartz'),
        ('sandstone', 'Sandstone'),
        ('simplex', 'Simplex'),
        ('sketchy', 'Sketchy'),
        ('slate', 'Slate'),
        ('solar', 'Solar'),
        ('spacelab', 'Spacelab'),
        ('superhero', 'Superhero'),
        ('united', 'United'),
        ('vapor', 'Vapor'),
        ('yeti', 'Yeti'),
        ('zephyr', 'Zephyr')
    ])
    image = FileField('Vaša slika', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Samo slike!')])


class UserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(3, 64), Email()])
    first_name = StringField("Ime", validators=[DataRequired(), Length(max=50)])
    last_name = StringField("Prezime", validators=[DataRequired(), Length(max=50)])
    is_confirmed = BooleanField('Potvrđen')
    bio = TextAreaField("Biografija", validators=[Length(max=1000)], render_kw={"id": "markdown-editor"})
    image = FileField('Slika', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Samo slike!')])
    submit = SubmitField("Spremi")