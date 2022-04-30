import os

class Config:

    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SOURCE_URL="https://newsapi.org/v2/top-headlines/sources category={}?apiKey={}"
    ARTICLE_URL="https://newsapi.org/v2/top-headlines?country={}&apiKey={}"


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}