from flask import Flask
#Flask, turn this file into a web application
#and give me a variable called app via which to reference it.

app = Flask(__name__)


#This particular function is not going to take any arguments,
#so all it's going to do is return a string or str of text, hello comma world

@app.route("/")
def index():
    return "hello, world"
# this is just some relatively little Python code,
#albeit using a couple of new features, a new library
#now
# new file Let me go ahead and run code of requirements.txt.
#And in this file, I'm going to simply specify what are all of the libraries
#that I want this web application to use
# ; not this index(): and double _ and _ means __
