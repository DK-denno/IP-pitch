from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,RadioField,SubmitField,TextAreaField,TextField
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
    submit = SubmitField('Submit')

class Comment(FlaskForm):
    username = StringField('username',validators=[Required()], render_kw={"placeholder": "USERNAME"})
    comments = TextField('Comment' ,validators=[Required()], render_kw={"placeholder": "COMMENT"})
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

