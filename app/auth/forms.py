from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class Signup(FlaskForm):
    Email = StringField('EMAIL-address',validators=[Required()])
    Username = StringField('USERNAME',validators=[Required()])
    Password = PasswordField('password',validators=[Required(), EqualTo('password2',message = 'Passwords must match')])    
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('SIGN UP')

    def validate_new_account(self,data_field):
        if User.query.filter_by(username=data_field.data).first() and User.query.filter_by(email=data_field.data).first():
            raise ValidationError('USERNAME OR EMAIL IS ALREADY TAKEN')
    


class Login(FlaskForm):
    Username = StringField('USERNAME',validators=[Required()])
    Password = PasswordField('password',validators=[Required()])
    submit = SubmitField('SIGN UP')
