from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    title = "Home"
    user = {'username': 'Unicorn'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",title=title,user=user,posts=posts)
