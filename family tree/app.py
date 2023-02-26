from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "Tejas" 
    age = "13.6"

    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def home():

    name = "Sumit"
    age = "38"

    return render_template('index.html' , name = name , age = age)

@app.route("/mother")
def home():

    name = "Lucky"
    age = "35"

    return render_template('index.html' , name = name , age = age)

@app.route("/friend")
def home():

    name = "Aarush"
    age = "14"

    return render_template('index.html' , name = name , age = age)

if __name__  ==  '__main__':
    app.run(debug=True)
