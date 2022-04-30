import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None
# Getting the movie base url
suorl = None
auorl=None

def configure_request(app):
    global api_key,suorl,auorl
    api_key = app.config['NEWS_API_KEY']
    suorl = app.config['SOURCE_URL']
    auorl=app.config['ATRICLE_URL']
