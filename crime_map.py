from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

DB = DBHelper()


@app.route("/")
def home():
    data = DB.get_all_inputs()
    return render_template('Home.html', data=data)


@app.route("/submitcrime", methods=['POST'])
def add_crime():
    category = request.form.get('category')
    date = request.form.get('date')
    latitude = float(request.form.get('latitude'))
    longitude = float(request.form.get('longitude'))
    description = request.form.get('description')
    DB.add_input(category, date, latitude, longitude, description)
    return home()


@app.route("/add", methods=['POST'])
def add():
    try:
        data = request.form.get('userinput')
        DB.add_input(data)
    except Exception as e:
        print(e)
    return home()


@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
