from flask import render_template
from . import main
from .. import auth
from ..models import Posts
from flask_login import login_required



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


