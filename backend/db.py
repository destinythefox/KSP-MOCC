import sqlite3

# Function to create a new flight record in the database and return the FlightID
def create_new_flight():
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO flights (timestamp) VALUES (CURRENT_TIMESTAMP)
    """)
    
    conn.commit()
    flight_id = cursor.lastrowid
    conn.close()
    
    return flight_id

# Function to write station data to the database for a given flight and station
def write_station_data(flight_id, station_name, data):
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO station_data (FlightID, StationName, Data)
    VALUES (?, ?, ?)
    """, (flight_id, station_name, data))
    
    conn.commit()
    conn.close()
