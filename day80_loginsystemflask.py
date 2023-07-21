

# from flask import Flask,request

# app = Flask(__name__)

# @app.route('/process', methods=["POST"])

# def process():
#   page = ""
#   form = request.form
#   if form["baldies"]=="David":
#     page += f"You're alright {form['username']}"
#   else:
#     page+= f"You've picked wrong, {form['username']}"
    
#   return page


# @app.route('/')

# def index():
#   page = """<form method = "post" action="/process">
#     <p>Name: <input type="text" name="username" required> </p>
#     <p>Email: <input type="Email" name="email"> </p>
#     <p>Website: <input type="url" name="website"> </p>
#     <p>Age: <input type="number" name="age"> </p>
#     <input type="hidden" name="userID" value="232"> </p>

#     <p>
#       Fave Baldy: 
#       <select name="baldies">
#         <option>David</option>
#         <option>Jean Luc Picard</option>
#         <option>Yul Brynner</option>
#       </select>
#     </p>

#     <button type="submit">Save Data</button>
#   </form>
#     """
#   return page
  
# app.run(host='0.0.0.0', port=81)


# from flask import Flask,request

# app = Flask(__name__)

# @app.route('/process', methods=["POST"])

# def process():
#   page = ""
#   form = request.form
#   if form["baldies"]=="David":
#     page += f"You're alright {form['username']}"
#   else:
#     page+= f"You've picked wrong, {form['username']}"
    
#   return page


# @app.route('/')

# def index():
#   page = """<form method = "post" action="/process">
#     <p>Name: <input type="text" name="username" required> </p>
#     <p>Email: <input type="Email" name="email"> </p>
#     <p>Website: <input type="url" name="website"> </p>
#     <p>Age: <input type="number" name="age"> </p>
#     <input type="hidden" name="userID" value="232"> </p>

#     <p>
#       Fave Baldy: 
#       <select name="baldies">
#         <option>David</option>
#         <option>Jean Luc Picard</option>
#         <option>Yul Brynner</option>
#       </select>
#     </p>

#     <button type="submit">Save Data</button>
#   </form>
#     """
#   return page
  
# app.run(host='0.0.0.0', port=81)



from flask import Flask,request

app = Flask(__name__)

logins = {}
logins["david"] = {"email" : "a@a.com", "password" : "baldy1"}
logins["katie"] = {"email" : "b@a.com", "password" : "k8t"}
logins["yul"] = {"email" : "c@a.com", "password" : "etc"}




@app.route('/login', methods =["POST"])
def login():
  form = request.form
  is_there = False
  details = {}
  try:
    details  = logins[form["username"]]
    is_there = True
  except:
    return "Username, email or password incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return " You are logged in "
  else:
    return "Username, email or password incorrect."

@app.route('/')

def index():
  page = """<form method = "post" action="/process">
        <p>Username : <input type="text" name="username" required></p>
        <p>Email : <input type="email" name="email" required></p>
        <p>Password : <input type="password" name="password" required></p>
        <button type="submit">Login</button>



    </form>
    
    """
  return page
  
app.run(host='0.0.0.0', port=81)