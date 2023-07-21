from flask import Flask

app = Flask(__name__)

@app.route('/<pageNumber>')

def index(pageNumber):
  return f"This is page {pageNumber}"