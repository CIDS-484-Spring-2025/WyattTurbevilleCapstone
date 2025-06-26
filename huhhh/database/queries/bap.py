from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT TestID FROM test 
        ORDER BY TestID DESC
        LIMIT 1;
    """

    cursor.execute(query)
    result = cursor.fetchall()
    TestID = result[0]['TestID']

    query = """
        INSERT INTO bap (TestID, CFU, xhem, typeCount, size, color)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    params = [
        TestID,
        form_data['CFU'],
        form_data['xhem'],
        form_data['typeCount'],
        form_data['size'],
        form_data['color']
        ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        DELETE FROM bap
        WHERE (TestID = %s)
    """

    params = [row_data]

    cursor.execute(query, params)

    query = """
        DELETE FROM plate
        WHERE (TestID = %s)
    """

    cursor.execute(query, params)

    query = """
        DELETE FROM test
        WHERE (TestID = %s)
    """

    cursor.execute(query, params)

    connection.commit()

    cursor.close()
    connection.close()

def update_entry(row_data, row_id):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        UPDATE bap
        SET CFU = %s, xhem = %s, typeCount = %s,
        size = %s, color = %s
        WHERE (TestID = %s)
    """

    params = [
        row_data['CFU'],
        row_data['xhem'],
        row_data['typeCount'],
        row_data['size'],
        row_data['color'],
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()