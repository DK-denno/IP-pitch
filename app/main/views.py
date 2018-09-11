from flask import render_template,redirect,url_for,request
from . import main
from .. import auth
from .. import db,photos
from ..models import Posts,User,Comments
from flask_login import login_required,current_user
from .forms import Post,Comment,UpdateProfile


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
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(user_name = uname).first()

    
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(user_name = uname).first()
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.user_name))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST','GET'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(user_name = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/comments/<int:id>',methods = ['GET','POST'])
def comment(id):
    
    comm = Comment()
    if comm.validate_on_submit():
        feedback =  Comments(comment=comm.comments.data,pitch_id=id,user_id=current_user.id)    
        feedback.save_comment()
        comment_itself = Comments.query.filter_by(pitch_id=id)
        return render_template('comments.html',comm = comm,comment_itself=comment_itself)
       
    return render_template('comments.html',comm = comm)

