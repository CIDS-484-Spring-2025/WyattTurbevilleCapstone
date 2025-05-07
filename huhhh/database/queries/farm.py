from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        INSERT INTO farm (FarmID)
        VALUES (%s)
    """

    params = [form_data['FarmID']]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()

def delete_entry(row_data):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        DELETE FROM farm
        WHERE (FarmID = %s)
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
        UPDATE farm
        SET FarmID = %s
        WHERE (FarmID = %s)
    """

    params = [
        row_data['FarmID'], 
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()