from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "keep it sacret, keep it safe"


@app.route('/')
def index():
    mysql = connectToMySQL('pets_flask_db')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template('index.html', all_pets=pets)


@app.route('/add_pet', methods=["POST"])
def add_pet_to_db():
    mysql = connectToMySQL('pets_flask_db')

    query = "INSERT INTO pets (name , type) values (%(name)s, %(type)s);"

    data = {
        # "id": request.form["pet_id"],
        "name": request.form["pet_name"],
        "type": request.form["pet_type"]
    }

    new_pet_id = mysql.query_db(query, data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
