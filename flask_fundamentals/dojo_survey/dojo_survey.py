from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', method=["POST"])
def add_user():
    is_valid = True
    if len(request.form['fname']) < 1:
        is_valid = False
        flash("Please enter a first name")
        return redirect('/')
    if len(request.form['lname']) < 1:
        is_valid = False
        flash("Please enter a last name")
        return redirect('/')
    if len(request.form['comment']) < 3:
        is_valid = False
        flash("comment should be at least 3 characters")
        return redirect('/')

    if is_valid:
        # add user to database
        mysql = connectToMySQL("dojo_survey")

        query = "INSERT INTO survey (surveyer_fname , surveyer_lname, dojo_location, favorite_language , comment) values (%(fn)s , %(ln)s, %(loc)s, %(flang)s , %(com)s); "

        data = {
            "fn": request.form["fname"],
            "ln": request.form["lname"],
            "loc": request.form["location"],
            "flang": request.form["language"],
            "com": request.form["comment"]
        }

        new_survey = mysql.query_db(query, data)
        flash("Friend successfully added!")

    return redirect('/result')


@app.route('/result')
def print_survey():
    # print("Got Post Info for the Survey")
    # print(request.form)
    # name_survey = request.form['name']
    # location_survey = request.form['location']
    # language_survey = request.form['language']
    # comment_survey = request.form['comment']
    mysql = connectToMySQL("dojo_survey")
    surveys = mysql.query_db("SELECT * FROM survey;")

    # , name_template=name_survey, location_template=location_survey, language_template=language_survey, comment_template=comment_survey)
    return render_template('result.html', surveys=surveys)


if __name__ == "__main__":
    app.run(debug=True)
