from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        INSERT INTO storage (Box, Spot, Date)
        VALUES (%s, %s, %s)
    """

    params = [
        form_data['Box'],
        form_data['Spot'],
        form_data['Date']
    ]

    cursor.execute(query, params)

    LocationID = cursor.lastrowid

    query = """
        UPDATE plate
        SET LocationID = %s
        WHERE (TestID = %s)
    """

    params = [
        LocationID,
        form_data['TestID']
    ]

    cursor.execute(query, params)

    if cursor.rowcount == 0:
        raise ValueError(f"No rows updated - TestID not found")

    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        UPDATE plate
        SET LocationID = NULL
        WHERE (LocationID = %s)
    """

    params = [row_data]

    cursor.execute(query, params)

    query = """
        DELETE FROM storage
        WHERE (LocationID = %s)
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
        UPDATE storage
        SET Box = %s, Spot = %s, Date = %s
        WHERE (LocationID = %s)
    """

    params = [
        row_data['Box'],
        row_data['Spot'],
        row_data['Date'],
        row_id
    ]

    cursor.execute(query, params)

    connection.commit()

    cursor.close()
    connection.close()