from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index = True)
    user_name = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    posts = db.relationship('Posts',backref = 'author',lazy = "dynamic")
    comments = db.relationship('Comments',backref = 'author',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('YOU CANNOT ACCESS THIS DETAILS')

    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    @login_manager.user_loader
    def load_user(id):
       return User.query.get(int(id))
    
class Posts(UserMixin,db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
   

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls,id):
        posts = Posts.query.all()
        return posts


class Comments(UserMixin,db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.all()
        return comments




    