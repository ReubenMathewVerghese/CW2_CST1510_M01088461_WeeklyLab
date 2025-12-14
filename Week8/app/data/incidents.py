import pandas as pd
from app.data.db import connect_database

def insert_incident(id, date, incident_type, severity, status):
    """
    Adds a new incident record to the database and returns the new ID.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = """
        INSERT INTO cyber_incidents 
        (id, date, incident_type, severity, status)
        VALUES (?, ?, ?, ?, ?)
    """
    values = (id, date, incident_type, severity, status)
    
    cursor.execute(sql, values)
    db.commit()
    db.close()


def update_incident(id, date, incident_type, severity, status):
    """
    Updates an existing incident record in the database.
    Returns True if successful, False otherwise.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = """
        UPDATE cyber_incidents
        SET date = ?, incident_type = ?, severity = ?, status = ?
        WHERE id = ?
    """
    values = (date, incident_type, severity, status, id)
    
    cursor.execute(sql, values)
    db.commit()

    # 3. Check if any row was updated
    success = cursor.rowcount > 0
    
    db.close()
    return success

def delete_incident(incident_id):
    """
    Deletes an incident record from the database by its ID.
    Returns True if successful, False otherwise.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = "DELETE FROM cyber_incidents WHERE id = ?"
    cursor.execute(sql, (incident_id,))
    db.commit()

    # 3. Check if any row was deleted
    success = cursor.rowcount > 0
    
    db.close()
    return success