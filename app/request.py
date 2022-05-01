
import urllib.request,json
import os

from .models import Source,Article

# Getting api key
# 
api_key='0264a9c2fe044a6497d9450ca0f12cc2'
# Getting the movie base url
# suorl = None
suorl='https://newsapi.org/v2/top-headlines/sources?apiKey={}&pageSize=10'
auorl='https://newsapi.org/v2/top-headlines?category=business&apiKey={}'

def configure_request(app):
    
    global api_key,suorl,auorl
    # api_key = app.config['NEWS_API_KEY']
    
    # suorl = app.config['SOURCE_URL']
    
    # auorl=app.config['ARTICLE_URL']



def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sourceurl = suorl.format(api_key)

    with urllib.request.urlopen(sourceurl) as url:
        souced= url.read()
        sourceres= json.loads(souced)

        source_results = None

        if sourceres['sources']:
            source_list = sourceres['sources']
            source_results = process(source_list)


    return source_results

def process(source_list):
    '''
    Function  that processes the  source results and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source in source_list:
        id = source.get('id')
        name=source.get('name')
        description=source.get('description')
        category=source.get('category')
        url=source.get('url')
        lang=source.get('language')
        country=source.get('country')

        if lang=="en":
            source_object = Source(id,name,description,lang,country,category,url)
            source_results.append(source_object)

    return source_results



#fetching the articles
def get_articles():
    ariclesurl=auorl.format(api_key)
    with urllib.request.urlopen(ariclesurl) as url:
        jdata=url.read()
        data= json.loads(jdata)

        articles_result= None
        if data['articles']:
            aricle_list=data['articles']
            articles_result=proc(aricle_list)
    return articles_result


def proc(lista):
    aricles_result=[] 
    for l in lista:
        source=l.get('source')
        title=l.get('title')
        author=l.get('author')
        des=l.get('description')
        content=l.get('content')
        url= l.get('url')
        image=l.get('urlToImage')
        publish=l.get('publishedAt')
        if source:
            article_object=Article(source,title,author,des,image,publish,content,url)
            aricles_result.append(article_object)
    return aricles_result
    print(aricles_result)


