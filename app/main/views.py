from flask import render_template,request,redirect,url_for
from . import main


# index route
@main.route('/')
def index():

    title="highlights"

    return render_template('index.html', title=title)