
# main.py

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    connection = sqlite3.connect('cars.db')
    cursor = connection.cursor()
    cars = cursor.execute('SELECT * FROM cars').fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', cars=cars)

@app.route('/car_details/<car_id>')
def car_details(car_id):
    connection = sqlite3.connect('cars.db')
    cursor = connection.cursor()
    car = cursor.execute('SELECT * FROM cars WHERE car_id=?', (car_id,)).fetchone()
    cursor.close()
    connection.close()
    return render_template('car_details.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
