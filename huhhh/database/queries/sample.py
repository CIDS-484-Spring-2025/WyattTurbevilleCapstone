from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        INSERT INTO sample (SampleID, CollectionDate, Quarter, Size, Is_Frozen, BacteriaID, CowID, FarmID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    params = [
        form_data['SampleID'],
        form_data['CollectionDate'],
        form_data['Quarter'],
        form_data['Size'],
        form_data['Is_Frozen'],
        form_data['BacteriaID'],
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
        DELETE FROM sample
        WHERE (SampleID = %s)
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
        UPDATE sample
        SET SampleID = %s, CollectionDate = %s, Quarter = %s, 
        Size = %s, Is_Frozen = %s, BacteriaID = %s, CowID = %s, FarmID = %s
        WHERE (SampleID = %s)
    """

    params = [
        row_data['SampleID'],
        row_data['CollectionDate'],
        row_data['Quarter'],
        row_data['Size'],
        row_data['Is_Frozen'],
        row_data['BacteriaID'],
        row_data['CowID'],
        row_data['FarmID'],
        row_id
    ]

    cursor.execute(query, params)
    connection.commit()

    cursor.close()
    connection.close()