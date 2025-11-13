import importlib
from flask import Flask, json, redirect, render_template, request, url_for
from extension import EnumManager
from database.query_util import (
    renderModal, renderSearch, renderTable, getStudySample, getStudySampleList
)

app = Flask(__name__)
enum = EnumManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/load-content/<page>')
def load_content(page):
    if page == "searchbar":
        return render_template("searchbar.html")
    elif page == "sample":
        table_data = renderTable(page)
        tag_data = getStudySample()
        return render_template('table.html', table_data=table_data, tag_data=tag_data)
    else :
        table_data = renderTable(page)
        return render_template('table.html', table_data=table_data)
    
@app.route('/load-search')
def load_search(page, results):
    if page == "dashboard":
        return render_template("dashboard.html")
    elif page == "sample":
        tag_data = getStudySample()
        return render_template('table.html', table_data=results, tag_data=tag_data)
    else :
        return render_template('table.html', table_data=results)

@app.route('/create-data/<table>', methods = ['GET'])
def create_data(table):
    table_data = renderModal(table)
    if table == "Sample":
        tag_data = renderTable('Study')
    else: tag_data = None
    try:
        form_choices = enum.get_table_choices(table)
        return render_template("createModal.html", table_data=table_data,
            form_choices=form_choices, table_name=table, tag_data=tag_data)
    except ValueError as e:
        return render_template("createModal.html", table_data=table_data,
            table_name=table, tag_data=tag_data)

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
        row_data = request.get_json()
        RowID = row_data['RowID']
        try:
            table_module = importlib.import_module(f'database.queries.{table}')
            table_module.delete_entry(RowID)
        except:
            return redirect('/failure')
        return '', 200
    
@app.route('/update-data/<table>', methods = ['POST'])
def updateData(table):
    row_data = request.get_json() #contains the SampleID
    table_data = renderModal(table) #Describe table
    if table == "Sample":
        tag_data = renderTable('Study') #all studyID's ever
        row_id = row_data['SampleID']
        row_tag_data = getStudySampleList(row_id)
        print(row_tag_data)
    else: 
        tag_data = None
        row_tag_data = None
    try:
        form_choices = enum.get_table_choices(table)
        return render_template("updateModal.html", table_data=table_data,
            row_data=row_data, form_choices=form_choices, table_name=table,
            tag_data=tag_data, row_tag_data=row_tag_data)
    except ValueError as e:
        return render_template("updateModal.html", table_data=table_data,
            row_data=row_data, table_name=table, tag_data=tag_data,
            row_tag_data=row_tag_data)
    
@app.route('/update-row/<table>', methods = ['POST'])
def updateRow(table):
    try:
        if table == "Sample":
            study_ids = request.form.getlist('StudyIDs[]')
        else: study_ids = None
        form_data = request.form.to_dict()
        first_key = next(iter(form_data))
        row_id = form_data.pop(first_key)

        if ('Is_Frozen' not in form_data):
            form_data['Is_Frozen'] = '0'

        table_module = importlib.import_module(f'database.queries.{table}')

        if study_ids != None:
            table_module.update_entry(form_data, row_id, study_ids)
        else:
            table_module.update_entry(form_data, row_id)
    except Exception as e:
        return redirect('/failure')
    return redirect('/success')

@app.route('/success')
def success_page():
    return "Form submitted successfully!"

@app.route('/failure')
def failure_page():
    return "Form submission encountered error!"

@app.route('/search-table/<table>', methods = ['GET'])
def searchTable(table):
    search_terms = request.args.get('column-names', '')
    print(f"Handed Table: {table}")
    try:
        search_data = renderSearch(table, search_terms)
        return load_search(results=search_data, page=table)
    except Exception as e:
        return redirect('/failure')

@app.template_filter('startswith')
def startswith_filter(s, prefix):
    return s.startswith(prefix)

if __name__ == '__main__':
    app.run()