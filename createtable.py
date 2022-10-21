import pandas as pd
import sqlite3
import csv


# Connecting to the database
connection = sqlite3.connect('nbagames.db')
 
# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()
 
# Table Definition
create_table = '''CREATE TABLE games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player TEXT NOT NULL,
                year INTEGER NOT NULL,
                team TEXT NOT NULL,
                role TEXT NOT NULL,
                mvp TEXT NOT NULL,
                orginalteam TEXT NOT NULL);
                '''
 
# Creating the table into our
# database
cursor.execute(create_table)
 
# Opening the person-records.csv file
file = open('nbaallstargames.csv')
 
# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)
 
# SQL query to insert data into the
# person table
insert_records = "INSERT INTO games (player, year, team, role, mvp, orginalteam) VALUES(?, ?, ?, ?, ?, ?)"
 
# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)
 
# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM games"
rows = cursor.execute(select_all).fetchall()
 
# Output to the console screen
for r in rows:
    print(r)
 
# Committing the changes
connection.commit()
 
# closing the database connection
connection.close()