import sqlite3
from datetime import datetime

DATABASE_NAME = "bmi_records.db"


def create_database():
    """Create the BMI records table if it does not exist."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_bmi_record(name, weight, height, bmi, category):
    """Save a BMI calculation to the database."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO bmi_records
        (name, weight, height, bmi, category, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category, date))

    connection.commit()
    connection.close()


def get_bmi_history():
    """Get all saved BMI records."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, weight, height, bmi, category, date
        FROM bmi_records
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records