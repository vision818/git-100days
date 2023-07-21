from flask import Flask, redirect, session, request
from replit import db
import os

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.environ['secretKey']

def getBlogs():
  entry = ""
  f = open("entry.html", "r")
  entry = f.read()
  f.close()
  keys = db.keys()
  keys = list(keys)
  content = ""
  for key in reversed(keys):
    thisEntry = entry
    if key != "user":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      content += thisEntry
  return content
      

@app.route('/')
def index():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  f = open("blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{content}", getBlogs())
  return page

@app.route('/loginForm')
def loginForm():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  f = open("login.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/login', methods=["POST"])
def login():
  if session.get("user"):
    return redirect("/edit")
  form = request.form
  if form["username"] == db["user"]["username"] and form["password"] == db["user"]["password"]:
    session["user"] = True
    return redirect("/edit")
  else:
    return redirect("/loginForm")

@app.route("/edit")
def edit():
  if not session.get("user"):
    return redirect("/")
  page = ""
  f = open("edit.html", "r")
  page = f.read()
  page = page.replace("{content}", getBlogs())
  f.close()
  return page

@app.route("/add", methods=["POST"])
def add():
  form = request.form
  entry = {"title": form["title"], "date" : form["date"], "body": form["body"]}
  db[form["date"]] = entry
  return redirect("/edit")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")

app.run(host='0.0.0.0', port=81)
