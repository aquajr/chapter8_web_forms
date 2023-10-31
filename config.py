import os 


class Config(object):
   """def app configurations"""
   SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'