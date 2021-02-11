from flask import Blueprint, render_template

# corresponds to using the Router middleware of Express.js.
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')