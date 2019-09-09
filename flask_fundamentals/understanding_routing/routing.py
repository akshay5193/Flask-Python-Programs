from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_word():
    return render_template('index.html', phrase="hello", times=5)


@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/say/<name>')
def hi(name):
    print(type(name))
    if(str(name)):
        return "Hi " + name + "!"

    return "Please enter valid name"


@app.route('/repeat/<number>/<message>')
def repeat_message(message, number=0):
    print(f"Message '{message}'' will be repeated {number} times below: ")
    return message * int(number)


app.run(debug=True)
