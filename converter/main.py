import sqlite3
import os

def query_panchang(date, location):
    # Build full path to the DB
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db', 'calendar.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT tithi, paksha, month, nakshatra, festival
        FROM panchang
        WHERE gregorian_date = ? AND location = ?
    ''', (date, location))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'tithi': row[0],
            'paksha': row[1],
            'month': row[2],
            'nakshatra': row[3],
            'festival': row[4] or "None"
        }
    else:
        return None

if __name__ == '__main__':
    date = input("Enter Gregorian date (YYYY-MM-DD): ")
    location = input("Enter location (e.g., HYD): ")
    result = query_panchang(date, location)

    if result:
        print(result)
    else:
        print("No data found for that date and location.")
