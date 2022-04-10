from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['TEMPLATES_AUTO_RELOAD'] = True

csrf = CSRFProtect(app)

POSTS = {
    0 : {
            'text': "text 0",
            'header': "Post header 0",
            'timestamp': datetime.now()
        },
    1 : {
            'text': "text 1",
            'header': "Post header 1",
            'timestamp': datetime.now()
        }
}

@app.route('/')
def index():
    return render_template('index.html', posts=POSTS)

@app.route('/post/new', methods=['GET', 'POST'])
def post_new():
    if request.method == 'POST':
        print (request.form.get("text"))
        POSTS[max(POSTS.keys()) + 1] = {
            'text': request.form.get("text"),
            'header': request.form.get("header"),
            'timestamp': datetime.now()
        }
        return redirect(url_for('index'))
    else:
        return render_template('new_post.html')

@app.route('/post/<int:post_id>', methods=['GET'])
def post(post_id):
    post = POSTS.get(post_id, None)
    return render_template('post.html', post=post)