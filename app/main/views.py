from flask import render_template
from . import main
from .forms import Signup,Login
from ..models import Posts

@main.route('/')
def index():
   
    title = 'one'
    
    return render_template('index.html',title=title)

@main.route('/signup')
def signup():
    form_signup = Signup()
    return render_template('signup.html',Signup=form_signup)

@main.route('/login')
def login():
    log_in = Login()
    return render_template('login.html',login=log_in)
    
# @main.route('/posts',methods=['GET','POST'])
# def get_posts():
#     '''creating a new instance of the Post class imported from app.models
#     '''
#     posts = Posts(id,title,post,category)
#     '''
#     saving the new post to the database
#     '''
#     posts.save_posts()
#     return render_template('post.html')


