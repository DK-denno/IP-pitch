from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class Posts(FlaskForm):
    title = StringField('PITCH NAME',validators=[Required()])
    post = StringField('POST',validators=[Required()])


