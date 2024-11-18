import mysql.connector

def verify_login(username, password, type):
    print(username, password, type)
    return True

def register_user(user, clubname, password):
    print(user, clubname, password)
    return True

def last_booking_id():
    return 4

def get_clubname(username):
    #agar username ek admin ho to 'ADMIN' return krna nhito clubname (keep in capital letters)
    return 'ADMIN'

def fetch_data(from_date, to_date):
    #agar from date aur to date None h then return full database otherwise filter and return list of tuples. (in python NULL is None)

    #for testing purposes
    lst = [(1, 'LT1', 'TIEDC', '10-11-2024', '12-11-2024', '10:00', '12:00', 'Pending'),
           (2, 'LT2', 'ACM', '10-11-2024', '12-11-2024', '10:00', '12:00', 'Pending'),
           (3, 'LT3', 'IEEE', '10-11-2024', '12-11-2024', '10:00', '12:00', 'Pending'),
           (4, 'LT1', 'ACM', '13-11-2024', '15-11-2024', '10:00', '12:00', 'Pending')]
    return lst

def add_data(record):
    #isme kuch return nhi krna , ye record basically ek tuple h with all the records usko database m dal de
    #return true if succesfully added and return false if there is a conflict

    #for testing purposes
    print(record)

    return False