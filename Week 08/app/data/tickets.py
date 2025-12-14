import csv
from pathlib import Path
import app.data.db as db
import pandas as pd

def get_all_tickets(filter: str):
    conn = db.connect_database()
    df = pd.read_sql_query(f"SELECT * from IT_Tickets WHERE {filter}", conn)
    conn.close()
    
    return df

def insert_ticket(t_id: str, sub: str, prio: str, status: str, cr_date: str):
    conn = db.connect_database()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO It_Tickets (ticket_id, subject, priority, status, created_date) 
                      VALUES (?, ?, ?, ?, ?)""", (t_id, sub, prio, status, cr_date))
    conn.commit()
    conn.close()
    

def update_ticket(id: str, new_id: str, new_sub: str, new_prio: str, new_stat: str, new_date: str):
    conn = db.connect_database()
    cursor = conn.cursor()
    cursor.execute(f"""UPDATE IT_Tickets
                    SET ticket_id = ?, subject = ?, priority = ?, status = ?, created_date = ?
                    WHERE ticket_id = ?""", (new_id, new_sub, new_prio, new_stat, new_date, id))
    cursor.execute("SELECT * FROM IT_Tickets ORDER BY ticket_id desc")
    print(cursor.fetchone())
    conn.commit()
    conn.close()


def delete_ticket(id: str):
    conn = db.connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM It_Tickets WHERE ticket_id = ?", (id, ))
    print(cursor.fetchone())
    conn.commit()
    conn.close()

def transfer_csv():
    conn = db.connect_database()
    cursor = conn.cursor()
    with open(Path("Week 08/DATA/it_tickets.csv").resolve()) as it_file:
        reader = csv.reader(it_file)
        header: bool = True
        for row in reader:
            if header == True:
                header = False
                continue
            cursor.execute("INSERT INTO It_Tickets (ticket_id, subject, priority, status, created_date) VALUES (?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4]))
        
    conn.commit()
    conn.close()