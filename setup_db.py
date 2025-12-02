import mysql.connector

try:
    # Connect to MySQL without specifying a database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123"
    )
    cursor = conn.cursor()
    
    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS menstrual_tracker")
    print("✓ Database 'menstrual_tracker' created successfully!")
    
    cursor.close()
    conn.close()
except Exception as e:
    print(f"✗ Error: {e}")
    print("Make sure MySQL is running and credentials are correct.")
