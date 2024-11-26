from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"


#FILTERS
#safe
#lower
#upper
#capitalize
#title
#trim
#striptags

def index():
    first_name = "Naman"
    stuff =  "This is <strong>Bold</strong> text."
    stuff1 = "This is bold text." 
    favourite_pizza = ["Onion","Classic","Chesse",41]
    return render_template("index.html", first_name=first_name,
    stuff=stuff,
    stuff1=stuff1,
    favourite_pizza=favourite_pizza)

#localhost:5000/user/Naman
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500