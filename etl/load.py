import sqlite3
import pandas as pd

# Define the path to the SQLite database
db_path = '../database/activity_tracking.db'

# Connect to the SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Function to load a CSV file into an SQLite table
def load_csv_to_sqlite(csv_path, table_name, conn):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Convert the DataFrame to SQL
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Define your CSV paths and corresponding table names
csv_files = {
    '../data/processed/activities.csv': 'Activities',
    '../data/processed/activity_types.csv': 'ActivityTypes',
    '../data/processed/performance_metrics.csv': 'PerformanceMetrics',
    '../data/processed/lap_metrics.csv': 'LapMetrics',
    '../data/processed/elevation_metrics.csv': 'ElevationMetrics'
}

# Define the table schemas with primary and foreign keys
table_schemas = {
    'Activities': '''
        DROP TABLE IF EXISTS Activities;
        CREATE TABLE Activities (
            ActivityID INTEGER PRIMARY KEY,
            ActivityTypeID INTEGER,
            Date DATETIME,
            Title TEXT,
            FOREIGN KEY (ActivityTypeID) REFERENCES ActivityTypes(ActivityTypeID)
        );
    ''',
    'ActivityTypes': '''
        DROP TABLE IF EXISTS ActivityTypes;
        CREATE TABLE ActivityTypes (
            ActivityTypeID INTEGER PRIMARY KEY,
            ActivityType TEXT
        );
    ''',
    'PerformanceMetrics': '''
        DROP TABLE IF EXISTS PerformanceMetrics;
        CREATE TABLE PerformanceMetrics (
            PerformanceID INTEGER PRIMARY KEY,
            ActivityID INTEGER,
            ActivityTypeID INTEGER,
            Distance REAL,
            Calories REAL,
            Time REAL,
            AvgHR INTEGER,
            MaxHR INTEGER,
            AerobicTE REAL,
            AvgRunCadence REAL,
            AvgPace REAL,
            BestPace REAL,
            FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID),
            FOREIGN KEY (ActivityTypeID) REFERENCES ActivityTypes(ActivityTypeID)
        );
    ''',
    'LapMetrics': '''
        DROP TABLE IF EXISTS LapMetrics;
        CREATE TABLE LapMetrics (
            LapID INTEGER PRIMARY KEY,
            ActivityID INTEGER,
            BestLapTime REAL,
            NumberOfLaps INTEGER,
            TotalDistance REAL,
            LapDistance REAL,
            MovingTime REAL,
            ElapsedTime REAL,
            FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID)
        );
    ''',
    'ElevationMetrics': '''
        DROP TABLE IF EXISTS ElevationMetrics;
        CREATE TABLE ElevationMetrics (
            ElevationMetricID INTEGER PRIMARY KEY,
            ActivityID INTEGER,
            TotalAscent INTEGER,
            TotalDescent INTEGER,
            MinElevation INTEGER,
            MaxElevation INTEGER,
            FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID)
        );
    '''
}

# Execute table schema scripts
for table_name, table_schema in table_schemas.items():
    cursor.executescript(table_schema)

# Load CSV files into SQLite database
for csv_path, table_name in csv_files.items():
    load_csv_to_sqlite(csv_path, table_name, conn)

# Commit changes and close the connection
conn.commit()
conn.close()

print("CSV files have been successfully loaded into the SQLite database.")