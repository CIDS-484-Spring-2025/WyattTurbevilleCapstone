import importlib
from flask import Flask, redirect, render_template, request
from extension import EnumManager
from database.query_util import (
    renderModal, renderTable
)

app = Flask(__name__)
enum = EnumManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/load-content/<page>')
def load_content(page):
    if page == "dashboard":
        return render_template("dashboard.html")
    else :
        table_data = renderTable(page)
        return render_template('table.html', table_data=table_data)

@app.route('/create-data/<table>', methods = ['GET'])
def create_data(table):
    try:
        table_data = renderModal(table)
        form_choices = enum.get_table_choices(table)
        return render_template("createModal.html", table_data=table_data,
            form_choices=form_choices)
    except ValueError as e:
        return render_template("createModal.html", table_data=table_data)

@app.route('/create-data/<table>', methods = ['POST'])
def createData(table):
    form_data = request.form
    try:
        # Dynamically import the module
        table_module = importlib.import_module(f'database.queries.{table}')
        # Call the module's create_entry function
        table_module.create_entry(form_data)
    except Exception as e:
        return redirect('/failure')
    return redirect('/success')

@app.route('/delete-data/<table>', methods = ['POST'])
def deleteData(table):
    if request.method == 'POST':
        row_data = request.data.decode('utf-8')
        try:
            table_module = importlib.import_module(f'database.queries.{table}')
            table_module.delete_entry(row_data)
        except:
            return redirect('/failure')
        return '', 200
    
@app.route('/update-data/<table>', methods = ['POST'])
def updateData(table):
    try:
        row_data = request.get_json()  
        table_data = renderModal(table)
        form_choices = enum.get_table_choices(table)
        return render_template("updateModal.html", table_data=table_data,
            row_data=row_data, form_choices=form_choices)
    except ValueError as e:
        return render_template("updateModal.html", table_data=table_data,
            row_data=row_data)
    
@app.route('/update-row/<table>', methods = ['POST'])
def updateRow(table):
    try:
        form_data = request.form.to_dict()
        first_key = next(iter(form_data))
        row_id = form_data.pop(first_key)

        if ('Is_Frozen' not in form_data):
            form_data['Is_Frozen'] = '0'

        table_module = importlib.import_module(f'database.queries.{table}')
        table_module.update_entry(form_data, row_id)
    except Exception as e:
        app.logger.error(f"Route error: {str(e)}", exc_info=True)
        return redirect('/failure')
    return redirect('/success')

@app.route('/success')
def success_page():
    return "Form submitted successfully!"

@app.route('/failure')
def failure_page():
    return "Form submission encountered error!"

@app.template_filter('startswith')
def startswith_filter(s, prefix):
    return s.startswith(prefix)

if __name__ == '__main__':
    app.run()