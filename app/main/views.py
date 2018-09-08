from flask import render_template
from . import main
from .. import auth
from ..models import Posts
from flask_login import login_required
from .forms import Post


@main.route('/')

def index():
   
    title = 'one'
    
    return render_template('index.html',title=title)

@main.route('/pitch',methods=['GET','POST'])
@login_required
def pitch():
    '''
    displaying the pitching form
    '''
    pitch = Post()
    pitches = Posts(title=pitch.title.data,post=pitch.post.data)
    pitches.save_post()

    title = 'PITCH-FORM'



    return render_template('pitch.html',pitch=pitch,title=title)
