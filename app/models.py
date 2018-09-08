from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255))
    user_name = db.Column(db.String(255))
    password = db.Column(db.Integer)
    posts = db.relationship('Posts',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comments',backref = 'user',lazy = "dynamic")
class Posts(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.String(255))
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls,id):
        posts = Posts.query.all()
        return posts


class Comments(db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
