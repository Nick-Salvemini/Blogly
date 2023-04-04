"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag
from sqlalchemy import text

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'chickens'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    users = User.query.all()
    return render_template('home.html', users=users)

# Routes for Users -------------------------------------

@app.route('/create_user')
def go_to_create_user():
    return render_template('create_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    image_url = request.form['imageUrl']
    new_user = User(first_name = first_name, last_name = last_name, image_url = image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f'/{new_user.id}')

@app.route('/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404({user_id})
    posts = Post.query.filter_by(user_id=user.id)
    return render_template('details.html', user = user, posts=posts)

@app.route('/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get_or_404({user_id})
    return render_template('edit_user.html', user = user)

@app.route('/<int:user_id>/edit', methods=['POST'])
def post_edit_user(user_id):
    user = User.query.get_or_404({user_id})
    user.first_name = request.form['editFirstNameInput']
    user.last_name = request.form['editLastNameInput']
    user.image_url = request.form['urlInput']
    db.session.add(user)
    db.session.commit()
    return render_template('details.html', user = user)

@app.route('/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404({user_id})
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

# Routes for Posts ---------------------------------

@app.route('/posts/<int:post_id>')
def post_details(post_id):
    post = Post.query.get_or_404({post_id})
    user = User.query.get_or_404({post.user_id})
    tags = Post.query.get({post_id}).tags_available
    return render_template('post.html', post=post, user=user, tags=tags)

@app.route('/new_post/<int:user_id>')
def new_post(user_id):
    user = User.query.get_or_404({user_id})
    tags = Tag.query.all()
    return render_template('new_post.html', user=user, tags=tags)

@app.route('/new_post/<int:user_id>', methods=['POST'])
def post_new_post(user_id):
    user = User.query.get_or_404({user_id})
    title = request.form['titleText']
    content = request.form['contentText']
    tags = Tag.query.all()
    selected_tags =[]
    for tag in tags:
        if request.form.get(f'tag{tag.id}'):
            selected_tags.append(tag)
    new_post = Post(title=title, content=content, user_id=user.id, tags_available=selected_tags)

    db.session.add(new_post)
    db.session.commit()

    
    return redirect(f'/posts/{new_post.id}')

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    post = Post.query.get_or_404({post_id})
    user = User.query.get_or_404({post.user_id})
    tags = Tag.query.all()
    post_tags = PostTag.query.all()
    return render_template('edit_post.html', post=post, user=user, tags=tags, post_tags=post_tags)

# ^^^ add tags to edit page ----------------------

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def post_edit_post(post_id):
    post = Post.query.get_or_404({post_id})
    user = User.query.get_or_404({post.user_id})
    tags = Tag.query.all()
    selected_tags =[]
    for tag in tags:
        if request.form.get(f'tag{tag.id}'):
            selected_tags.append(tag)
    post.title = request.form['titleText']
    post.content = request.form['contentText']
    post.tags_available = selected_tags
    db.session.add(post)
    db.session.commit()
    return render_template('post.html', post=post, user=user, tags=selected_tags)

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404({post_id})
    user = User.query.get_or_404({post.user_id})
    db.session.delete(post)
    db.session.commit()
    return redirect(f'/{user.id}')

# Routes for Tags -----------------------------------------------------
# List All Tags
@app.route('/all_tags')
def list_all_tags():
    tags = Tag.query.all()
    return render_template('all_tags.html', tags=tags)

# Show Posts with Tag
@app.route('/posts/<tag_name>')
def posts_by_tag(tag_name):
    post_tag = Tag.query.filter(Tag.name == {tag_name}).one()
    tag_id = post_tag.id
    posts = Post.query.filter(Tag.id == {tag_id}).all()
    return render_template('tag_posts', posts=posts)

# Create Tag
@app.route('/new_tag')
def new_tag():
    return render_template('new_tag.html')

@app.route('/new_tag', methods=['POST'])
def post_new_tag():
    tag_name = request.form['tagName']
    new_tag = Tag(name=tag_name)
    db.session.add(new_tag)
    db.session.commit()
    return redirect('/')

# Edit Tag
@app.route('/edit_tag/<tag_name>')
def edit_tag(tag_name):
    return render_template('edit_tag.html')

@app.route('/edit_tag/<tag_name>', methods=['POST'])
def post_edit_tag(tag_name):
    tag = Tag.query.filter(Tag.name == {tag_name}).one()
    tag.name = request.form['tagName']
    db.session.add(tag)
    db.session.commit()
    return redirect('/')