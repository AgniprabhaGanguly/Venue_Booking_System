import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Database connection
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12126519',
        database='Venue_Booking_System'
    )
    if conn.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error connecting to database: {e}")
    conn = None

def verify_login(userid, password, type):
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE userid = %s AND password = %s AND type = %s"
        cursor.execute(query, (userid, password, type))
        user = cursor.fetchone()
        if user == None:
            return False
        else:
            return True
    except Error as e:
        print(f"Database error: {e}")
        return False

def register_user(userid, clubname, password):
    try:
        cursor = conn.cursor()
        # Check if the username already exists
        check_query = "SELECT * FROM users WHERE userid = %s"
        cursor.execute(check_query, (userid,))
        if cursor.fetchone():
            return False

        # Insert new user into the database
        insert_query = "INSERT INTO users (userid, username, password, type) VALUES (%s, %s, %s, 'CLUB')"
        cursor.execute(insert_query, (userid, clubname, password))
        conn.commit()
        return True
    except Error as e:
        print(f"Database error: {e}")
        return False

def get_username(userid):
    try:
        cursor = conn.cursor()
        query = "select username from users where userid =%s"
        cursor.execute(query, (userid,))
        user = cursor.fetchone()
        return user[0]
    except Error as e:
        print(f"Database error: {e}")
        return None

def fetch_user_type(userid):
    try:
        cursor = conn.cursor()
        query = "select type from users where userid = %s"
        cursor.execute(query, (userid,))
        user = cursor.fetchone()
        return user[0]
    except Error as e:
        print(f"Database error: {e}")
        return None

def last_booking_id():
    cursor = conn.cursor()
    query = "SELECT * FROM venue"
    cursor.execute(query)
    bookings = cursor.fetchall()
    last_row_index = len(bookings) - 1
    return bookings[last_row_index][0]

def fetch_data(from_date, to_date):
    try:
        cursor = conn.cursor()  # Use dictionary=True for better readability
        if not from_date and not to_date:
            query = "SELECT * FROM venue"
            cursor.execute(query)
        else:
            query = "SELECT * FROM venue WHERE from_date >= %s AND to_date <= %s"
            cursor.execute(query, (from_date, to_date))

        rows = cursor.fetchall()
        print(rows)
        return rows

    except Error as e:
        print(f"Database error: {e}")
        return None

def add_data(record):
    #return true false
    try:
        cursor = conn.cursor()
        bookingid,venue,bookedby, from_date, to_date, from_time, to_time, status = record
        print(record)
        conflict_query ="SELECT COUNT(*) FROM VENUE WHERE VENUE=%s AND ((from_date <= %s AND to_date >= %s)OR(from_date >= %s AND from_date <= %s)Or(to_date >= %s AND to_date <= %s))"
        cursor.execute(conflict_query, (venue, to_date, from_date, from_date, to_date, to_date, from_date))
        conflict_count = cursor.fetchone()[0]
        if conflict_count >0:
            print("conflict detected")
            return False
        else:
            insert_query = """INSERT INTO VENUE (bookingid,venue,bookedby,from_date, to_date,from_time,to_time,status)
               VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"""
        cursor.execute(insert_query,record)
        conn.commit()
        print("data inserted")
        return True

    except Error as e:
        print(f"Database error: {e}")
        return None

def delete_data(record, user_id):
    try:
        if (record[2] == user_id) or (fetch_user_type(user_id)=='ADMIN'):
            cursor = conn.cursor()
            query = "DELETE FROM VENUE WHERE bookingid=%s"
            cursor.execute(query, list(record[0]))
            conn.commit()
            print("data deleted")
            return True
        else:
            print('User conflict')
            return False
    except Error as e:
        print(f"Database error: {e}")
        return False

def update_status(bookingid, status):
    try:
        cursor = conn.cursor()
        query = "UPDATE VENUE SET status = %s WHERE bookingid = %s"
        cursor.execute(query, (status, bookingid))
        conn.commit()
        print("data updated")
        return True
    except Error as e:
        print(f"Database error: {e}")
        return False

def change_password(userid, old_password, new_password):
    try:
        cursor = conn.cursor()
        #check query
        query = "SELECT * FROM users WHERE userid = %s AND password = %s"
        cursor.execute(query, (userid, old_password))
        user = cursor.fetchone()
        if user:
            query = "UPDATE users SET password = %s WHERE userid = %s"
            cursor.execute(query, (new_password, userid))
            conn.commit()
            print("data updated")
            return True
        else:
            print("User current password do not match")
            return False
    except Error as e:
        print(f"Database error: {e}")
        return False
