from flask import render_template,redirect,url_for
from . import main
from .. import auth
from ..models import Posts
from flask_login import login_required
from .forms import Post,Comment


@main.route('/')

def index():
   
    title = 'one'
    all = Posts.query.all()
    return render_template('index.html',title=title,posts=all)

@main.route('/pitch',methods=['GET','POST'])
@login_required
def pitch():
    '''
    displaying the pitching form
    '''
    pitch = Post()
    if pitch.validate_on_submit():  
      
        pitches = Posts(title=pitch.title.data,post=pitch.post.data,category=pitch.category.data)
        pitches.save_post()
        return redirect(url_for('main.index'))

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
    
    return render_template('political.html',pitches=Political)


@main.route('/pick-up-lines',methods = ['GET','POST'])
def pick():
    '''
    displaying pitches themselves
    '''
    pickup = Posts.query.filter_by(category="pick-up-lines").all()
    
    return render_template('pickup.html',pitches=pickup )

# @main.route('/comments/<int:id>')
# def comment(id):
#     comment_post = Posts.query.filter_by(id = posts.id).first()
#     comm = Comment()
#     if comm.validate_on_submit():
#         feedback =  Comments(comment=form.comments.data)    
#         feedback.save_comment()
#         comment_itself = Comments.query.all()
#         return render_template('comments.html',comm = comm,comment_itself=comment_itself,comment=comment_post)
#     return render_template('comments.html',comm = comm,comment=comment_post)

