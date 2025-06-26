import re
from database import get_db_connection

def renderModal(table):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    query = f"DESCRIBE {table}"

    cursor.execute(query)

    table_data = cursor.fetchall()

    filtered_columns = [
        col for col in table_data 
        if 'auto_increment' not in col['Extra'].lower()
        and col['Field'].lower() != 'testid'
    ]

    cursor.close()
    connection.close()

    return filtered_columns

def renderSchema():
    return None    

def renderTable(page):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True) 

    query = f"""
        SELECT *
        FROM {page};
    """

    cursor.execute(query)

    table_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return table_data

def renderSearch(table, search_terms):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    #exists for future checking to see if searched column is valid
    column_list = renderModal(table)
    column_names = [row['Field'] for row in column_list]

    terms = search_terms.split()
    qfrom = [table]
    qwhere = []
    qorder = []
    qparts = []

    for term in terms:
        if re.search(r':', term):
            if re.search(r'[=<>]', term):
                match = re.match(r'(\w+):([<>]=?|=)([\w-]+)', term)
                if match:
                    column, operator, value = match.groups()
                    result = f"{column} {operator} '{value}'"
                    qwhere.append(result)
            if re.search(r'(asc|desc)\s*$', term, re.IGNORECASE):
                column, condition = term.split(':')
                result = f"{column} {condition}"
                qorder.append(result)
            if re.search(r'(order)\s*$', term, re.IGNORECASE):
                column, condition = term.split(':')
                result = f"{column}"
                qorder.append(result)

    qparts.append("SELECT *")

    if qfrom:
        qparts.append("FROM " + table)

    if qwhere:
        qparts.append("WHERE " + " AND ".join(qwhere))

    if qorder:
        qparts.append("ORDER BY " + " AND ".join(qorder))

    #build query string from qparts
    if qparts:
        query = """ """ + " ".join(qparts) + ";"

    cursor.execute(query)

    search_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return search_data

def fullSearch(search_terms):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    terms = search_terms.split()
    qselect = []
    qfrom = []
    qwhere = []
    qorder = []
    qparts = []

    for term in terms:
        if re.search(r':', term):
            column, term = re.split(':', term)


    return None

def getStudySample():

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True) 

    query = """
        SELECT *
        FROM studysample;
    """

    cursor.execute(query)

    table_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return table_data

def getStudySampleList(SampleID):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True) 

    query = """
        SELECT StudyID
        FROM studysample
        WHERE (SampleID = %s)
    """

    params = [SampleID]

    cursor.execute(query, params)

    table_data = cursor.fetchall()

    study_ids = [row['StudyID'] for row in table_data]

    cursor.close()
    connection.close()

    return study_ids