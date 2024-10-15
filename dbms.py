import mysql.connector

def verify_login(username, password, type):
    print(username, password, type)
    return False

def register_user(user, clubname, password):
    print(user, clubname, password)