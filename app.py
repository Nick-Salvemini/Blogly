"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
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
    return render_template('details.html', user = user)

# @app.route('/edit')
# def create_user():
#     return render_template('edit.html')