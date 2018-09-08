from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,RadioField,SubmitField,TextField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class Post(FlaskForm):
    title = StringField('PITCH TITLE',validators=[Required()])
    post = TextField('POST',validators=[Required()])
    category = RadioField('Pick Category',
                          choices=[('Political', 'Political'),
                                ('Motivational', 'Motivational'),
                                   ('pick-up-lines', 'pick-up-lines')],
                          validators=[Required()])
    submit = SubmitField('Submit',validators=[Required()])

class Comment(FlaskForm):
    comment = TextField( validators=[Required()], render_kw={"placeholder": "COMMENT"})