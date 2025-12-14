def create_users_table(conn):
    """Create users table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    

def create_cyber_incidents_table(conn):
    """
    Create the cyber_incidents table.
    """
    
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cyber_Incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            incident_type TEXT,
            severity TEXT,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    
    print("SUCCCESS")


def create_datasets_metadata_table(conn):
    """
    Create the datasets_metadata table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Datasets_Metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_name TEXT NOT NULL,
            category TEXT,
            file_size_mb REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()


def create_it_tickets_table(conn):
    """
    Create the it_tickets table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS IT_Tickets (
            ticket_id TEXT PRIMARY KEY,
            subject TEXT NOT NULL,
            priority TEXT,
            status TEXT,
            created_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()


def create_all_tables() -> None:
    """
        Explanation: Creates Users, Cyber_Incidents, Datasets_Metadata, It_Tickets Tables in intelligence_platform.db
    """
    import sqlite3
    from pathlib import Path
    print(Path("Week 08/DATA/intelligence_data.db").resolve())
    conn = sqlite3.connect(Path("Week 08/DATA/intelligence_data.db").resolve())
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)