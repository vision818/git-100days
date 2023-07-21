from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  get = request.args
  if get["name"].lower() == "david":
    return "Hello baldie!"
  return "No data"

app.run(host = '0.0.0.0', port =81)