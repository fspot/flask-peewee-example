from flask import Flask
from settings import *

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return 'Hello !'

