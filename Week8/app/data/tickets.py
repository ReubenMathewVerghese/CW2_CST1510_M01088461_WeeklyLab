import csv
from pathlib import Path
import pandas as pd 
from app.data.db import connect_database

def insert_ticket(ticket_id, subject, priority, status, created_date):
    """
    Adds a new ticket record to the database matching the CSV structure.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = """
        INSERT INTO IT_Tickets 
        (ticket_id, subject, priority, status, created_date)
        VALUES (?, ?, ?, ?, ?)
    """
    values = (ticket_id, subject, priority, status, created_date)
    
    cursor.execute(sql, values)
    db.commit()
    db.close()

def getalltickets(filter: str):
    conn = connect_database()
    df = pd.read_sql_query("SELECT {column} from IT_Tickets WHERE {filter}", conn)
    conn.close()
    
    return df

def drop_tickets_table():
    """
    Drops the IT_Tickets table from the database.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = "DROP TABLE IF EXISTS IT_Tickets"
    
    cursor.execute(sql)
    db.commit()
    db.close()

def update_ticket(ticket_id, subject, priority, status, created_date):
    """
    Updates an existing ticket record in the database.
    Returns True if successful, False otherwise.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = """
        UPDATE IT_Tickets
        SET subject = ?, priority = ?, status = ?, created_date = ?
        WHERE ticket_id = ?
    """
    # The ticket_id goes last to match the WHERE clause
    values = (subject, priority, status, created_date, ticket_id)
    
    cursor.execute(sql, values)
    db.commit()

    # 3. Check if any row was updated
    success = cursor.rowcount > 0
    
    db.close()
    return success

def delete_ticket(ticket_id):
    """
    Deletes a ticket record from the database by its ticket_id.
    Returns True if successful, False otherwise.
    """
    # 1. Connect to the DB
    db = connect_database()
    cursor = db.cursor()

    # 2. Run the SQL Command
    sql = "DELETE FROM IT_Tickets WHERE ticket_id = ?"
    cursor.execute(sql, (ticket_id,))
    db.commit()

    # 3. Check if any row was deleted
    success = cursor.rowcount > 0
    
    db.close()
    return success

def transfercsv():
    conn = connect_database()
    cursor = conn.cursor()
    with open(Path("Week8/DATA/it_tickets.csv").resolve()) as itFile:
        reader = csv.reader(itFile)
        header: bool = True
        for row in reader:
            if header == False:
                header = False
                continue
            cursor.execute("INSERT INTO It_Tickets (ticket_id, subject, priority, status, created_date) VALUES (?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4]))
        
    conn.commit()
    conn.close()