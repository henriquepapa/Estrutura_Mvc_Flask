from app import db

class User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self,username,password,name,email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username



class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.Foreingnkey('users.id'))

    user = db.relationship ('User'), db.Foreingnkey(users_id)

    def __init__(self,content,id_user):
        self.content = content
        self.id_user = id_user

    def __repr__(self):
        return "<Post %r>" % self.id

class Follow(db.Model):
    __tablename__="follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.Foreingnkey('users.id'))
    follower_id = user_id = db.Column(db.Integer, db.Foreingnkey('users.id'))

    user = db.relationship('User'), db.Foreingnkey(users_id)
    follower_id = db.relationship('User'), db.Foreingnkey(users_id)

    def __init__(self,user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id

    def __repr__(self):
        return "<Follow %r>" % self.follower_id