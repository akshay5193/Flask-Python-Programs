from flask import Flask, redirect, render_template, flash, request, session
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def root():
    mysql = connectToMySQL("email_validation")
    emailids = mysql.query_db("SELECT * FROM emails;")
    # session['all_emailids'] = emailids

    return render_template('root.html', all_emailids=emailids)


@app.route('/validate', methods=["POST"])
def validate():

    # test whether a field matches the pattern
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
        return redirect('/')

    else:
        mysql = connectToMySQL("email_validation")
        data = {
            "em": request.form["email"]
        }
        query = "INSERT INTO emails (email) values (%(em)s); "

        new_email = mysql.query_db(query, data)
        flash("Great! That was a valid email.")
        return redirect('/')


@app.route('/delete/<id>')
def delete(id):
    mysql = connectToMySQL("email_validation")
    data = {
        "id": id
    }
    query = "DELETE FROM emails where email_id = %(id)s"

    mysql.query_db(query, data)
    print("********************* DELETED A ROW ************************")

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
