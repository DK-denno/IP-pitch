from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo

class Signup(FlaskForm):
    Email = StringField('EMAIL-address',validators=[Required()])
    Username = StringField('USERNAME',validators=[Required()])
    Password = PasswordField('password',validators=[Required(), EqualTo('password2',message = 'Passwords must match')])    
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('SIGN UP')

class Login(FlaskForm):
    Username = StringField('USERNAME',validators=[Required()])
    Password = PasswordField('password',validators=[Required(), EqualTo('password2',message = 'Passwords must match')])    
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('SIGN UP')

class Posts(FlaskForm):
    title = StringField('PITCH NAME',validators=[Required()])
    post = StringField('POST',validators=[Required()])


