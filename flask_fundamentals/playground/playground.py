from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    print("Hey, welcome to the playground!")
    return render_template('index.html')


@app.route('/play')
def play():
    phrase = "Please put the URL in following format: localhost:5000/play/(x)  -  where x is an integer number to create that many number of boxes on your screen"
    return render_template('index.html', phrase=phrase)


@app.route('/play/<number>')
def repeat_boxes(number):

    return render_template('index.html', number=int(number))


app.run(debug=True)
