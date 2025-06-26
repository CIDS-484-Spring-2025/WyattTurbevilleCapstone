from database import get_db_connection

def create_entry(form_data):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        INSERT INTO sample (CollectionDate, Quarter, Inoculum, Is_Frozen, BacteriaID, CowID, FarmID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    params = [
        form_data['CollectionDate'],
        form_data['Quarter'],
        form_data['Inoculum'],
        form_data['Is_Frozen'],
        form_data['BacteriaID'],
        form_data['CowID'],
        form_data['FarmID']
    ]

    cursor.execute(query, params)

    SampleID = cursor.lastrowid  

    study_ids = form_data.getlist('StudyIDs[]')

    for study_id in study_ids:
        query = """
            INSERT INTO studysample (StudyID, SampleID)
            VALUES (%s, %s)
        """
        params = (study_id, SampleID)
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

    query = """
        DELETE FROM studysample
        WHERE (SampleID = %s)
    """

    cursor.execute(query, params)

    connection.commit()

    cursor.close()
    connection.close()

def update_entry(row_data, row_id, study_ids):
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        UPDATE sample
        SET CollectionDate = %s, Quarter = %s, 
        Inoculum = %s, Is_Frozen = %s, BacteriaID = %s, CowID = %s, FarmID = %s
        WHERE (SampleID = %s)
    """

    params = [
        row_data['CollectionDate'],
        row_data['Quarter'],
        row_data['Inoculum'],
        row_data['Is_Frozen'],
        row_data['BacteriaID'],
        row_data['CowID'],
        row_data['FarmID'],
        row_id
    ]

    cursor.execute(query, params)

    query = """
        DELETE FROM studysample
        WHERE (SampleID = %s);
    """

    SampleID = row_id

    cursor.execute(query, (SampleID,))
    print('post-wipe')

    for study_id in study_ids:
        query = """
            INSERT INTO studysample (StudyID, SampleID)
            VALUES (%s, %s)
        """
        params = (study_id, SampleID)
        cursor.execute(query, params)


    connection.commit()

    cursor.close()
    connection.close()