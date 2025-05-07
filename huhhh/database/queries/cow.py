from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        INSERT INTO cow (CowID, FarmID)
        VALUES (%s, %s)
    """

    params = [
        form_data['CowID'], 
        form_data['FarmID']
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        DELETE FROM cow
        WHERE (CowID = %s)
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
        UPDATE cow
        SET CowID = %s, FarmID = %s
        WHERE (CowID = %s)
    """

    params = [
        row_data['CowID'],
        row_data['FarmID'],
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()