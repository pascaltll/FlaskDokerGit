from app import app
from flask import Flask, render_template, flash, redirect
import os
from app.forms import LoginForm

template_dir = os.path.abspath('app/template')

app = Flask(__name__,template_folder=template_dir)
app.config['SECRET_KEY'] = 'you-will-never-guess'
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
app.config.from_object(Config)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'JC'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/<name>")
def user(name):
    return f"hello {name}"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)