from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)

    first_name = db.Column(db.String(50),
                            nullable = False)

    last_name = db.Column(db.String(50),
                            nullable = False)

    image_url = db.Column(db.String,
                            nullable = False,
                            unique = True)
    
    def __repr__(self):
        u = self
        return f'<User - id = {u.id}, first_name = {u.first_name},last_name = {u.last_name},image_url = {u.image_url}>'

class Post(db.Model):
    __tablename__='posts'

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True) 

    title = db.Column(db.String(100),
                        nullable = False)

    content = db.Column(db.String(2000))

    created_at = db.Column(db.DateTime,
                            nullable = False,
                            default = func.now())

    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.id'),
                        nullable = False)
    
    user = db.relationship('User', 
                           backref='posts')
    
    tags_for_post = db.relationship('PostTag',
                                    backref='posts')
    
    tags_available = db.relationship('Tag',
                                     secondary='post_tags',
                                     backref='posts')
    
    def __repr__(self):
        p = self
        return f'<Post - Title:"{p.title}" (post id: {p.id}) posted by "{p.user_id}" at {p.created_at}: {p.content}>'
    
class Tag(db.Model):
    __tablename__='tags'

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    
    posts_for_tag = db.relationship('PostTag',
                                    backref='tags')
    
    def __repr__(self):
        t = self
        return f'<Tag - name = {t.name}, id = {t.id}>'
    
class PostTag(db.Model):
    __tablename__='post_tags'

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'),
                        primary_key=True,)

    tag_id = db.Column(db.Integer,
                        db.ForeignKey('tags.id'),
                        primary_key=True)
    
    def __repr__(self):
        pt = self
        return f'<Post ID: {pt.post_id}; Tag ID: {pt.tag_id}>'