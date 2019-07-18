from flask import Flask
from arxiv import feedback

app = Flask(__name__)
feedback.install(app)