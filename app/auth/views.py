from . import auth
from flask import render_template,redirect,url_for,flash
from ..models import User
from .forms import Signup,Login
from .. import db



@auth.route('/signup',methods= ['GET',' POST'])
def signup():
    register = Signup()
    if register.validate_on_submit():
        users = User(user_name=form.username.data,password=form.password.data) 
        db.session.add(users)
        db.session.commit()
        return render_template(url_for('auth.login'))


    return render_template('auth/signup.html',signup=register)

@auth.route('/login',methods=['GET','POST'])
def login():
    log_in = Login()
    if log_in.validate_on_submit():
        user = User.query.filter_by(user_name=log_in.username.data).first()
        if user is not None and user.verify_password(log_in.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')    
    
    return render_template('auth/login.html',login=log_in)