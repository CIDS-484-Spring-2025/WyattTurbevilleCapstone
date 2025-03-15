from flask import Flask, jsonify, render_template, request
import mysql.connector
app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'first_db',
    'port': 3306
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/paragraph', methods = ['POST'])
def send():
    if request.method == 'POST':
        #pull input values from index.html
        searchMin = request.form['searchMin']
        searchMax = request.form['searchMax']

        #connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT textcol FROM sentances WHERE id BETWEEN %s AND %s"
        cursor.execute(query, (searchMin, searchMax))

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        combined_string = '. '.join(row[0] for row in results)

        return render_template('paragraph.html', combined_string=combined_string)

if __name__ == '__main__':
    app.run()