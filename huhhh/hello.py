from flask import Flask, jsonify, render_template, request
import mysql.connector
app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'researchdb',
    'port': 3306
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/load-content/<page>')
def load_content(page):
    if page == "dashboard":
        return render_template("dashboard.html")
    elif page == "farm":
        table_data = renderFarm()
        return render_template('farm.html', table_data=table_data)
    else:
        return "<p>Page not found</p>", 404
    
def renderFarm():

    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor(dictionary=True) 

    query = """
        SELECT *
        FROM farm;
    """

    cursor.execute(query)

    table_data = cursor.execute(query)

    cursor.close()
    connection.close()

    return table_data

@app.route('/load-action/<table>/<action>')
def load_action(table, action):
    if action == "search":
        return render_template("modal.html")
    if action == "add":
        table_data = renderModal(table)
        return render_template("modal.html", table_data=table_data)
    if action == "update":
        return render_template("modal.html")
    if action == "delete":
        return render_template("modal.html")

def renderModal(table):

    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor(dictionary=True)

    query = f"DESCRIBE {table}"

    cursor.execute(query)

    form_data = cursor.execute(query)

    cursor.close()
    connection.close()

    return form_data

@app.route('/commit-data', methods = ['POST'])
def commitData():
    
    return

if __name__ == '__main__':
    app.run()