from flask import Flask
import datetime # import the datetime library

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/home') 
def home():
  today = datetime.date.today() # Get today's date
  page = f"""html 
  # Format the html as an fString
  <html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="day74_css.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1>Vision's Portfolio</h1>
  
  <h2>1. Day 21 - math Game</h2>

  <p> On day 21, we started getting familiar with python projrcts, and we built a project, which asks user for a math test and give them result according to their performance... </p>
  <img src = "files/day21.png"  width = "66%"></img>
  <p><a href = "https://replit.com/@vision818/day-21100-days"> the code </a></p>

  
  <h2>2. Day 34 - Pretty Printing </h2>

  <p> On day 34, I got to know about the other aspects about printing, how you can modify and visualize the print code using subroutine is amazing... </p>
  <img src = "files/day34.png"  width = "66%"></img>
  <p><a href = "https://replit.com/@vision818/day-34100-days"> the code </a></p>



  
  <h2>3. Day 35 - TODO list </h2>

  <p> On day 35, we created a todo list for a user, which includes adding, viewing, editing and deleting the data... </p>
  <img src = "files/day35.png"  width = "66%"></img>
  <p><a href = "https://replit.com/@vision818/day-35100-days"> the code </a></p>


  <h2>4. Day 57 - Recursion </h2>

  <p> On day 57, we got to know about Recursion, recursion is in itslelf is a good idea, using itself to create a subroutine, which gives new perspective to the code and allows to open new horizons... </p>
  <img src = "files/day57.png"  width = "66%"></img>
  <p><a href = "https://replit.com/@vision818/day-57100-days"> the code </a></p>



  
  <h2>5. Day 66 - calculator </h2>

  <p> On day 66, we created out first calculator, which is every programmers dream, and this is just starting of building massive amazing codes... </p>
  <img src = "files/day66.png"  width = "66%"></img>
  <p><a href = "https://replit.com/@vision818/day-66100-days"> the code </a></p>

  
</body>

</html>

  
  """