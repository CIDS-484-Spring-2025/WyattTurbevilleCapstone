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
        INSERT INTO mac (TestID, CFU, Lactose, TSI, M, I, O, CIT)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    params = [
        TestID,
        form_data['CFU'],
        form_data['Lactose'],
        form_data['TSI'],
        form_data['M'],
        form_data['I'],
        form_data['O'],
        form_data['CIT']
        ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        DELETE FROM mac
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
        UPDATE mac
        SET CFU = %s, Lactose = %s, TSI = %s,
        M = %s, I = %s, O = %s, CIT = %s
        WHERE (TestID = %s)
    """

    params = [
        row_data['CFU'],
        row_data['Lactose'],
        row_data['TSI'],
        row_data['M'],
        row_data['I'],
        row_data['O'],
        row_data['CIT'],
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()