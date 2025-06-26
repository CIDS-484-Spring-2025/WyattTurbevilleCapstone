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
        INSERT INTO gramstain (TestID, rods, cocci)
        VALUES (%s, %s, %s)
    """

    params = [
        TestID,
        form_data['rods'],
        form_data['cocci']
        ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        DELETE FROM gramstain
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
        UPDATE gramstain
        SET rods = %s, cocci = %s
        WHERE (TestID = %s)
    """

    params = [
        row_data['rods'],
        row_data['cocci'],
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()