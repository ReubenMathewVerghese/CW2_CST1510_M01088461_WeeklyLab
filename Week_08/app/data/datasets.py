import pandas as pd
from app.data.db import connect_database


def insert_dataset(id, name, category, file_size):
    """Insert new incident."""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO Datasets_Metadata 
        (id, dataset_name, category, file_size_mb)
        VALUES (?, ?, ?, ?)
    """, (id, name, category, file_size))
    
    conn.commit()
    incident_id = cursor.lastrowid
    conn.close()
    return incident_id


def get_all_datasets(filter: str):
    """
        Get all Datasets as DataFrame.
    """
    conn = connect_database()
    df = pd.read_sql_query(f"SELECT * FROM Datasets_Metadata WHERE {filter}", conn)
    conn.close()
    
    return df


def update_datasets(id: str, new_id: str, name: str, ctgry: str, new_size: str):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(f"""UPDATE Cyber_Incidents
                    SET id = ?, dataset_name = ?, category = ?, file_size_mb = ?
                    WHERE id = ?""", (int(new_id), name, ctgry, float(new_size), int(id)))
    conn.commit()
    conn.close()


def delete_dataset(id: str):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Datasets_Metadata WHERE id = ?", (int(id), ))
    conn.commit()
    conn.close()


def transfer_csv():
    import csv
    from pathlib import Path
    conn = connect_database()
    cursor = conn.cursor()
    with open(Path("Week 08/DATA/Datasets_Metadata.csv").resolve()) as it_file:
        reader = csv.reader(it_file)
        header: bool = True
        for row in reader:
            if header == True:
                header = False
                continue
            cursor.execute("INSERT INTO Datasets_Metadata (id, dataset_name, category, file_size_mb) VALUES (?, ?, ?, ?)", (int(row[0]), row[1], row[2], row[3]))

    conn.commit()
    conn.close()