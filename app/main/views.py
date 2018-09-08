from flask import render_template
from . import main
from .. import auth
from ..models import Posts
from flask_login import login_required
from .forms import Post


@main.route('/')
@login_required
def index():
   
    title = 'one'
    
    return render_template('index.html',title=title)


@main.route('/posts',methods=['GET','POST'])
def get_posts():
    '''creating a new instance of the Post class imported from app.models
    '''
    posts = Posts(id,title,post,category)
    '''
    saving the new post to the database
    '''
    posts.save_posts()
    return render_template('post.html')


@main.route('/pitch',methods=['GET','POST'])
def pitch():
    '''
    displaying the pitching form
    '''
    pitch = Post()
    title = 'PITCH-FORM'

    return render_template('pitch.html',pitch=pitch,title=title)
