import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://bloodpressuser:SzXPGJf4GTaJzvYH2by4gz0Ku9hiF6iN@dpg-cs0qvqogph6c73adlsrg-a.oregon-postgres.render.com/bloodpressdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
