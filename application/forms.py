from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Length, Email
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    username = StringField('username', validators = [DataRequired(), Length(max = 70)], description ='Username:', render_kw={"placeholder": "Seu username", "class": "form-control"})
    email = StringField('email', validators = [DataRequired(), Email(), Length(max = 70)], description ='Email:', render_kw={"placeholder": "Seu email", "class": "form-control"})
    password = PasswordField('password', validators = [DataRequired()], description ='Senha:', render_kw={"class": "form-control"})
    confirm = PasswordField('confirm', validators = [DataRequired(), EqualTo('password')],
        description='Confirme a senha:', render_kw={"class": "form-control", "oninput" : "verificaSenha()"})
    accept_tos = BooleanField('accept_tos', validators = [DataRequired(), InputRequired()],  description='Aceito os termos de serviço', 
        render_kw={"type": "checkbox"})