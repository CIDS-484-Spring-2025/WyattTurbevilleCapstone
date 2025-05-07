from database import get_db_connection

def renderModal(table):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    query = f"DESCRIBE {table}"

    cursor.execute(query)

    table_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return table_data

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