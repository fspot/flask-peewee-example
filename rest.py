from flask_peewee.rest import RestAPI, UserAuthentication
from app import app
from models import Note, Author

def setup_api(auth):
    user_auth = UserAuthentication(auth)
    api = RestAPI(app, default_auth=user_auth)
    api.register(Note)
    api.register(Author)
    api.setup()
    return api
