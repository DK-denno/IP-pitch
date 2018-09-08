from flask import render_template,redirect,url_for
from . import main
from .. import auth
from ..models import Posts
from flask_login import login_required
from .forms import Post,Comment


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
    pitches = Posts(title=pitch.title.data,post=pitch.post.data,category=pitch.category.data)
    pitches.save_post()
    

    title = 'PITCH-FORM'



    return render_template('pitch.html',pitch=pitch,title=title)

@main.route('/Motivational',methods = ['GET','POST'])
def pitches():
    '''
    displaying pitches themselves
    '''
    Motivational = Posts.query.filter_by(category="Motivational").all()
    
    return render_template('pitchess.html',pitches=Motivational)

@main.route('/Political',methods = ['GET','POST'])
def Political():
    '''
    displaying pitches themselves
    '''
    Political = Posts.query.filter_by(category="Political").all()
    print(pitchess)
    return render_template('political.html',pitches=Political)


@main.route('/pick-up-lines',methods = ['GET','POST'])
def pick():
    '''
    displaying pitches themselves
    '''
    pickup = Posts.query.filter_by(category="pick-up-lines").all()
    
    return render_template('pickup.html',pitches=pick-up )
