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
        INSERT INTO catalase (TestID, M, C, E, BE, CAMP)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    params = [
        TestID,
        form_data['M'],
        form_data['C'],
        form_data['E'],
        form_data['BE'],
        form_data['CAMP']
        ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        DELETE FROM catalase
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
        UPDATE catalase
        SET M = %s, C = %s, E = %s,
        BE = %s, CAMP = %s
        WHERE (TestID = %s)
    """

    params = [
        row_data['M'],
        row_data['C'],
        row_data['E'],
        row_data['BE'],
        row_data['CAMP'],
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()