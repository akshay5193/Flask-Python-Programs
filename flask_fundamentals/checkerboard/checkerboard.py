from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def checkerboard_home(number=8):
    return render_template('checkerboard.html', number=number)


# @app.route('/<rows>')
# def custom_rows(rows, number=8):
#     print(rows)
#     rows = int(rows)
#     return render_template('checkerboard.html', number=number, rows=rows)


TEMPLATES_AUTO_RELOAD = True
app.run(debug=True)
