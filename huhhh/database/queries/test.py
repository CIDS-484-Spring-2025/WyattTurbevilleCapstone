from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        INSERT INTO test (testType, ReadingDate, CultureDate, Is_Positive)
        VALUES (%s, %s, %s, %s)
    """

    params = [
        form_data['testType'],
        form_data['ReadingDate'],
        form_data['CultureDate']
    ]
    if 'Is_Positive' in form_data:
        params.append(form_data['Is_Positive'])
    else:
        params.append(None)

    cursor.execute(query, params)

    TestID = cursor.lastrowid

    query = """
        INSERT INTO plate (SampleID, TestID)
        VALUES (%s, %s)
    """

    params = [
        form_data['SampleID'],
        TestID
    ]

    cursor.execute(query, params)

    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    params = [row_data]

    query = """
        SELECT testType
        FROM test
        WHERE (TestID = %s);
    """

    cursor.execute(query, params)
    results = cursor.fetchall()
    testType = results[0]['testType']

    if testType != 'Prototheca':
        query = """
            DELETE FROM `%s`
            WHERE (TestID = %%s)
        """ % testType

        cursor.execute(query, (row_data,))

    query = """
        DELETE FROM plate
        WHERE (TestID = %s);
    """

    cursor.execute(query, params)

    query = """
        DELETE FROM test
        WHERE (TestID = %s);
    """

    cursor.execute(query, params)

    connection.commit()

    cursor.close()
    connection.close()

def update_entry(row_data, row_id):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        UPDATE test
        SET testType = %s, ReadingDate = %s, CultureDate = %s, Is_Positive = %s
        WHERE (TestID = %s)
    """

    params = [
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