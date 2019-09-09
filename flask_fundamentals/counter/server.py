from flask import Flask, rendering_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def home():
    return rendering_template('index.html')

@app.route('/counter', methods=['POST'])
def counter():
    print("Increased the visit count")
    session['number'] 