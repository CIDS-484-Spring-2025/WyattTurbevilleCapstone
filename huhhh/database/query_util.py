import re
from database import get_db_connection
from collections import deque

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

def simpleSearch(table, search_terms):

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

def fullSearch(search_terms):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    terms = search_terms.split()
    qwhere = []
    # waiting for me to code translation from column to table required
    # then insert that into the query statement

    for term in terms:
        if re.search(r':', term):
            if re.search(r'[=<>]', term):
                match = re.match(r'(\w+):([<>]=?|=)([\w-]+)', term)
                if match:
                    column, operator, value = match.groups()
                    # this is fine, column will just have to become table.column
                    table = matchTable(column)
                    result = f"{table}.{column} {operator} '{value}'"
                    qwhere.append(result)
    
    query = """
        SELECT
            s.*
        FROM
            researchdb.sample AS s
        INNER JOIN
            (
                -- Subquery to get the list of filtered SampleIDs
                SELECT distinct
                    s_inner.SampleID
                FROM
                    researchdb.sample AS s_inner
                INNER JOIN
                    cow AS c ON s_inner.CowID = c.CowID
                INNER JOIN
                    farm AS f ON c.FarmID = f.FarmID
                INNER JOIN
                    plate AS p ON s_inner.SampleID = p.SampleID
                INNER JOIN
                    test AS t ON p.TestID = t.TestID
                WHERE
                    -- Apply the filter using the farm table's alias
                    f.FarmID = '1'
            ) AS filteredid
            ON s.SampleID = filteredid.SampleID;
    """

    cursor.execute(query)

    search_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return search_data

def matchTable(column):

    aliasMap = {
        
    }

def searchPath(target):
    startTable = 'Sample'
    graph = {
        'Sample': ['StudySample', 'Cow', 'Plate'],
        'StudySample': ['Study'],
        'Study': [],
        'Cow': ['Farm'],
        'Farm': [],
        'Plate': ['Storage', 'Test'],
        'Storage': [],
        'Test': ['BAP', 'MAC', 'GramStain', 'Prototheca'],
        'BAP': [],
        'MAC': [],
        'GramStain': [],
        'Prototheca': []
    }

    if startTable == target:
        return [startTable]
    
    queue = deque([(startTable, [startTable])])
    visited = {startTable}

    while queue:
        current_table, path_so_far = queue.popleft()

        for neighbor in graph.get(current_table, []):

            if neighbor == target:
                return path_so_far + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                
                new_path = path_so_far + [neighbor]
                
                queue.append((neighbor, new_path))

    return None