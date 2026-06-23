import sqlite3
import random
from datetime import datetime, timedelta

def create_mock_database():
    conn = sqlite3.connect('healthcare_jobs.db')
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_jobs (
        job_id TEXT,
        client_name TEXT,
        direction TEXT,
        scheduled_time TEXT,
        status TEXT,
        error_log TEXT
    )
    ''')
    cursor.execute('DELETE FROM daily_jobs') # Clear old data on rerun

    clients = ['Client Alpha', 'Client Beta', 'Client Gamma']
    directions = ['Inbound (HL7)', 'Outbound (837P)']
    
    # Generate 15 mock jobs
    for i in range(15):
        job_type = random.choice(['D1', 'D2', 'D3'])
        client = random.choice(clients)
        direction = random.choice(directions)
        
        # Simulate an 80% success rate
        is_success = random.random() > 0.2
        status = 'Success' if is_success else 'Failed'
        
        # Inject realistic network/API errors for failures
        errors = [
            "HTTP 408: Request Timeout on target server.",
            "SSL Handshake Failed: Certificate expired.",
            "Payload Error: Invalid JSON format detected in client file."
        ]
        error_log = "N/A" if is_success else random.choice(errors)
        
        time_str = (datetime.now() - timedelta(minutes=random.randint(10, 300))).strftime('%H:%M')

        cursor.execute('''
        INSERT INTO daily_jobs (job_id, client_name, direction, scheduled_time, status, error_log)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (job_type, client, direction, time_str, status, error_log))

    conn.commit()
    conn.close()
    print("Mock database 'healthcare_jobs.db' created successfully.")

if __name__ == "__main__":
    create_mock_database()