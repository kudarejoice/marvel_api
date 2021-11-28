import os 

basedir = os.path.abspath(os.path.dirname(__file__))

#Gives access to the project and allows outside folders/files to be added to the project from the base directory

class Config():
    """
        Set Config variables for the flask app by using the Environment variables where available otherwise creaate the config variable.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Turns off updated messages from sqlalchemy