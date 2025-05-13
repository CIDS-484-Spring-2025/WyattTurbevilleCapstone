from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        INSERT INTO test (TestID, testType, ReadingDate, CultureDate, Is_Positive)
        VALUES (%s, %s, %s, %s, %s)
    """

    params = [
        form_data['TestID'],
        form_data['testType'],
        form_data['ReadingDate'],
        form_data['CultureDate'],
        form_data['Is_Positive']
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        DELETE FROM test
        WHERE (TestID = %s)
    """

    params = [row_data]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def update_entry(row_data, row_id):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        UPDATE test
        SET TestID = %s, testType = %s, ReadingDate = %s, CultureDate = %s, Is_Positive = %s
        WHERE (TestID = %s)
    """

    params = [
        row_data['TestID'],
        row_data['testType'],
        row_data['ReadingDate'],
        row_data['CultureDate'],
        row_data['Is_Positive'],
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()