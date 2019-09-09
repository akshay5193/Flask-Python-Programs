from flask import Flask, render_template, request, redirect
import os

img_folder = os.path.join('static', 'img')

app = Flask(__name__)
app.config['upload_folder'] = img_folder


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']
    raspberry_form = request.form['raspberry']
    strawberry_form = request.form['strawberry']
    apple_form = request.form['apple']
    return render_template("checkout.html", first_name_template=first_name_from_form, last_name_template=last_name_from_form, student_id_template=student_id_from_form, raspberry_template=raspberry_form, strawberry_template=strawberry_form, apple_template=apple_form)


@app.route('/fruits')
def fruits():
    strawberry = os.path.join(app.config['upload_folder'], 'strawberry.png')
    raspberry = os.path.join(app.config['upload_folder'], 'raspberry.png')
    blackberry = os.path.join(app.config['upload_folder'], 'blackberry.png')
    apple = os.path.join(app.config['upload_folder'], 'apple.png')
    return render_template("fruits.html", strawberry=strawberry, raspberry=raspberry, blackberry=blackberry, apple=apple)


if __name__ == "__main__":
    app.run(debug=True)
