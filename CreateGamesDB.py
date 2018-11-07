import sqlite3
from sqlite3 import Error
####


# Defining tables for future use
def tables():
    sql_create_Games_table = """ CREATE TABLE IF NOT EXISTS Games(
        id integer PRIMARY KEY,
        name text NOT NULL,
        key text NOT NULL,
        platform text NOT NULL);"""
    return sql_create_Games_table


# connect to db
def createConnection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


# create tables
def create_table(conn, create_table_sql):
    # conn == connection defined in createConnection
    # create table == SQL CREATE TABLE statement
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# Create example data
def example_data(conn):
    exampledata = ('ExampleGame', '1111-1111-1111-111', 'Steam')
    sql = '''INSERT INTO Games(name, key, platform)
            VALUES (?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, exampledata)


# main program
def main():
    db_file = "gameKeys.db"
    conn = createConnection(db_file)
    if conn is not None:
        sqltable = (tables())
        create_table(conn, sqltable)
        print("Table created\n")
    else:
        print("Error: connection to DB not made")
    print("Add example data? y/n\n")
    userIn = str(input())
    if userIn == "y":
        example_data(conn)
