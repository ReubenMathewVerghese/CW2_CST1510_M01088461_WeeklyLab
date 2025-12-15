import pandas as pd
from app.data.db import connect_database


def insert_incident(date, incident_type, severity, status):
    """Insert new incident."""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO cyber_incidents 
        (date, incident_type, severity, status)
        VALUES (?, ?, ?, ?)
    """, (date, incident_type, severity, status))
    
    conn.commit()
    incident_id = cursor.lastrowid
    conn.close()
    return incident_id


def get_all_incidents(filter: str):
    """
        Get all incidents as DataFrame.
        Takes filter: str as parameter and filters incidents
    """
    conn = connect_database()
    df = pd.read_sql_query(f"SELECT * FROM Cyber_Incidents", conn)
    conn.close()
    
    return df


def update_incident(id: str, new_id: str, inc_type: str, new_sev: str, new_stat: str, new_date: str):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(f"""UPDATE Cyber_Incidents
                    SET id = ?, incident_type = ?, severity = ?, status = ?, date = ?
                    WHERE id = ?""", (int(new_id), inc_type, new_sev, new_stat, new_date, int(id)))
    conn.commit()
    conn.close()


def delete_incident(id: str):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Cyber_Incidents WHERE id = ?", (int(id), ))
    conn.commit()
    conn.close()


def transfer_csv():
    import csv
    from pathlib import Path
    conn = connect_database()
    cursor = conn.cursor()
    with open(Path("Week 08/DATA/cyber_incidents.csv").resolve()) as it_file:
        reader = csv.reader(it_file)
        header: bool = True
        for row in reader:
            if header == True:
                header = False
                continue
            cursor.execute("INSERT INTO Cyber_Incidents (id, incident_type, severity, status, date) VALUES (?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4]))

    conn.commit()
    conn.close()