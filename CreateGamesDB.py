import sqlite3
from sqlite3 import Error
####


# Defining tables for future use
def tables():
    sql_create_Games_table = """ Create table Games(
        ID integer,
        Name text NOT NULL,
        Key text NOT NULL,
        Platform text NOT NULL,
        Primary key(ID))"""
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
        c.execute("select name from sqlite_master where name=Games")
        result = c.fetchall()
        keep_table = True
        if len(result) == 1:
            userIn = input("The table already exists, re-created it? y/n: ")
            userIn = userIn.lower()
            if userIn == "y":
                keep_table = False
                print("The table will be re-created, all data will be lost ")
                c.execute("drop table if exists Games")
                conn.commit()
            else:
                print("The exisitng table was kept")
        else:
            keep_table = False
        if not keep_table:
            c.execute(create_table_sql)
            conn.commit()
    except Error as e:
        print(e)


# Create example data
def example_data(conn):
    exampledata = ('ExampleGame', '1111-1111-1111-111', 'Steam')
    sql = '''INSERT INTO Games(name, key, platform)
            VALUES (?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, exampledata)
    conn.commit()


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


if __name__ == '__main__':
    main()
