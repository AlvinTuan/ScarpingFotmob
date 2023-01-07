import pandas as pd
import mysql.connector as msql
from mysql.connector import Error


try:
    connector = msql.connect(host = '127.0.0.1', user = 'root', password = '') #input ur username & password
    if connector.is_connected():
        cursor = connector.cursor()
        cursor.execute("CREATE DATABASE leagues")
        print('database is created')
except Error as err:
    print('Error while connecting to MySQL', err)


NAME_LEAGUES = ["EPL", "La_liga", "Bundesliga" , "Serie_A", "Ligue_1"]

for league in NAME_LEAGUES:

    lg = pd.read_csv(f'data/{league}/g-and-ga-{league}.csv', index_col = False, delimiter=',')
    # league.head()

    try:
        connector = msql.connect(host = '127.0.0.1', database = 'leagues', user = 'root', password = '') #input ur username & password
        if connector.is_connected():
            cursor = connector.cursor()
            cursor.execute("SELECT DATABASE(); ")
            record = cursor.fetchone()
            print("-------------------------------------------")
            print('You are connected to the database: ', record)
            cursor.execute(f'DROP TABLE IF EXISTS {league};')
            #creating the tables
            print(f'Creating the tables {league}')
            cursor.execute(f"CREATE TABLE  {league} (Team varchar(255) NOT NULL, G int NOT NULL, GA int NOT NULL);")
            print(f"Table {league} is created")

            #insert data
            for i,row in lg.iterrows():
                sql = f"INSERT INTO leagues.{league} VALUES (%s, %s, %s) "
                cursor.execute(sql, tuple(row))
                print('{i+1} -Data inserted')
                # the connection is not auto committed by default, so we must commit to save our changes
                connector.commit()
                
    except Error as err:
        print('Error while connecting to MySQL', err)



