import csv
from pathlib import Path
import pandas as pd 
from app.data.db import connect_database

def insert_metadata(dataset_name, category, file_size_mb):
    """
    Adds a new dataset metadata record to the database.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = """
        INSERT INTO Datasets_Metadata 
        (dataset_name, category, file_size_mb)
        VALUES (?, ?, ?)
    """
    values = (dataset_name, category, file_size_mb)
    
    cursor.execute(sql, values)
    db.commit()
    db.close()

def update_metadata(id, dataset_name, category, file_size_mb):
    """
    Updates an existing dataset metadata record in the database.
    Returns True if successful, False otherwise.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = """
        UPDATE Datasets_Metadata
        SET dataset_name = ?, category = ?, file_size_mb = ?
        WHERE id = ?
    """
    values = (dataset_name, category, file_size_mb, id)
    
    cursor.execute(sql, values)
    db.commit()

    # 3. Check if any row was updated
    success = cursor.rowcount > 0
    
    db.close()
    return success

def delete_metadata(id):
    """
    Deletes a dataset metadata record from the database by its ID.
    Returns True if successful, False otherwise.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = "DELETE FROM Datasets_Metadata WHERE id = ?"
    cursor.execute(sql, (id,))
    db.commit()

    # 3. Check if any row was deleted
    success = cursor.rowcount > 0
    
    db.close()
    return success

def getalldatasets(filter: str):
    """
        Get all Datasets as DataFrame.
    """
    conn = connect_database()
    df = pd.read_sql_query(f"SELECT * FROM Datasets_Metadata WHERE {filter}", conn)
    conn.close()
    
    return df

def transfercsv():
    import csv
    from pathlib import Path
    conn = connect_database()
    cursor = conn.cursor()
    with open(Path("Week8/DATA/Datasets_Metadata.csv").resolve()) as itFile:
        reader = csv.reader(itFile)
        header: bool = True
        for row in reader:
            if header == True:
                header = False
                continue
            cursor.execute("INSERT INTO Datasets_Metadata (id, dataset_name, category, file_size_mb) VALUES (?, ?, ?, ?)", (int(row[0]), row[1], row[2], row[3]))

    conn.commit()
    conn.close()