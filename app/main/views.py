from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources


# index route
@main.route('/')
def index():

    title="highlights"
    business_sources=get_sources()
    political_sources=get_sources()

    return render_template('index.html', title=title, political=political_sources)