# Import necessary libraries 
import pandas as pd
import sqlite3
import os

# Load csv file into pandas dataframe
activity_types_df = pd.read_csv('../data/processed/activity_types.csv')
activities_df = pd.read_csv('../data/processed/activities.csv')
performance_df = pd.read_csv('../data/processed/performance_metrics.csv')
laps_df = pd.read_csv('../data/processed/lap_metrics.csv')
elevation_df = pd.read_csv('../data/processed/elevation_metrics.csv')

# Creating SQLite database
conn = sqlite3.connect('../database/database.sqlite')
cursor = conn.cursor()

# Table Definition
create_table_1 = '''CREATE TABLE IF NOT EXISTS ActivityTypes(
                ActivityTypeID Text PRIMARY KEY,
                ActivityType Text NOT NULL);
                '''

# Creating the table into our database
cursor.execute(create_table_1)

# insert the data from the DataFrame into the SQLite table
activity_types_df.to_sql('ActivityTypes', conn, if_exists='replace', index = False)

# Printing pandas dataframe
pd.read_sql('''SELECT * FROM ActivityTypes''', conn)

# Table Definition
create_table_2 = '''CREATE TABLE IF NOT EXISTS Activities (
                ActivityID Integer PRIMARY KEY, 
                ActivityTypeID Text NOT NULL, 
                Date Datetime, 
                Title Text NOT NULL,
                FOREIGN KEY (ActivityTypeID) REFERENCES ActivityTypes (ActivityTypeID)
                );
                '''

# Creating the table into our database
cursor.execute(create_table_2)

# insert the data from the DataFrame into the SQLite table
activities_df.to_sql('Activities', conn, if_exists='replace', index = False)

# Printing pandas dataframe
pd.read_sql('''SELECT * FROM Activities''', conn)

# Table Definition
create_table_3 = '''CREATE TABLE IF NOT EXISTS PerformanceMetrics (
                PerformanceID Text PRIMARY KEY, 
                ActivityID Integer NOT NULL, 
                ActivityTypeID Text NOT NULL, 
                Distance Float NOT NULL, 
                Calories Float NOT NULL, 
                TimeMinutes Float NOT NULL, 
                AvgHR Integer NOT NULL, 
                MaxHR Integer NOT NULL, 
                AerobicTE Float NOT NULL, 
                AvgRunCadence Float NOT NULL, 
                AvgPaceMinKm Float NOT NULL, 
                BestPaceMinKm Float NOT NULL, 
                FOREIGN KEY (ActivityID) REFERENCES Activities (ActivityID), 
                FOREIGN KEY (ActivityTypeID) REFERENCES ActivityTypes (ActivityTypeID)
                );
                '''

# Creating the table into our database
cursor.execute(create_table_3)

# insert the data from the DataFrame into the SQLite table
performance_df.to_sql('PerformanceMetrics', conn, if_exists='replace', index = False)

# Printing pandas dataframe
pd.read_sql('''SELECT * FROM PerformanceMetrics''', conn)

# Table Definition
create_table_4 = '''CREATE TABLE IF NOT EXISTS LapMetrics (
                LapID Text PRIMARY KEY, 
                ActivityID Integer NOT NULL, 
                BestLapTimeMin Float NOT NULL, 
                NumberOfLaps Integer NOT NULL, 
                TotalDistanceKm Float NOT NULL, 
                LapDistanceKm Float NOT NULL, 
                MovingTimeMin Float NOT NULL, 
                ElapsedTimeMin Float NOT NULL, 
                FOREIGN KEY (ActivityID) REFERENCES Activities (ActivityID)
                );
                '''

# Creating the table into our database
cursor.execute(create_table_4)

# insert the data from the DataFrame into the SQLite table
laps_df.to_sql('LapMetrics', conn, if_exists='replace', index = False)

# Printing pandas dataframe
pd.read_sql('''SELECT * FROM LapMetrics''', conn)

# Table Definition
create_table_5 = '''CREATE TABLE IF NOT EXISTS ElevationMetrics (
                ElevationMetricID Text PRIMARY KEY, 
                ActivityID Integer NOT NULL, 
                TotalAscent Integer NOT NULL, 
                TotalDescent Integer NOT NULL, 
                MinElevation Integer NOT NULL, 
                MaxElevation Integer NOT NULL, 
                FOREIGN KEY (ActivityID) REFERENCES Activities (ActivityID)
                );
                '''

# Creating the table into our database
cursor.execute(create_table_5)

# insert the data from the DataFrame into the SQLite table
elevation_df.to_sql('ElevationMetrics', conn, if_exists='replace', index = False)

# Printing pandas dataframe
pd.read_sql('''SELECT * FROM ElevationMetrics''', conn)

# commit the changes and close the connection
conn.commit()

# close the connection
conn.close()

