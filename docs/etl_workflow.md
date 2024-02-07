## Project Overview:
The ETL (Extract, Transform, Load) process in this project involves extracting data from a single large CSV file called Activities.csv, which contains comprehensive activity tracking data. The data is then transformed into multiple CSV files representing different entities, such as activity types, performance metrics, lap metrics, and elevation metrics. These CSV files are subsequently loaded into a SQLite database for efficient data management and analysis.

### 1. Extraction:
All data is initially extracted from the main file, [Activities.csv](data/raw/Activities.csv). This file contains a wide range of information related to activity tracking sessions, including activity type, date, title, performance metrics, lap metrics, and elevation metrics.

### 2. Transformation:
The extracted data undergoes transformation to ensure it meets the desired format and schema. Various transformations are applied, including:

- **Data type conversions**: Convert date and time strings to datetime objects.
- **Cleaning missing or invalid values**: Remove rows with missing or invalid data.
- **Feature engineering**: Calculate additional metrics such as average pace and lap distance.
- **Data filtering**: Retain rows for specific activity types (e.g., Running and Swimming).
- **Concatenation of text columns for composite keys**: Combine Activity ID and Activity Type ID to create unique metric IDs.
- **Resetting DataFrame indices**: Reset DataFrame indices to ensure consistency and avoid index-related errors.

### 3. Loading:
Transformed data is exported to separate CSV files corresponding to different entities:

- **[activities.csv](data/processed/activities.csv)**: Contains basic details about each activity, such as activity ID, activity type ID, date, and title.
- **[activity_types.csv](data/processed/activity_types.csv)**: Provides a reference table for activity types, with unique activity type IDs and corresponding names.
- **[performance_metrics.csv](data/processed/performance_metrics.csv)**: Stores specific performance metrics for deeper analysis, including distance, calories burned, time, heart rate, and pace.
- **[lap_metrics.csv](data/processed/lap_metrics.csv)**: Captures lap-specific metrics such as lap time, number of laps, total distance, and moving/elapsed time.
- **[elevation_metrics.csv](data/processed/elevation_metrics.csv)**: Records elevation-related metrics, including total ascent, total descent, and minimum/maximum elevation.

### 4. SQLite Database Creation:
A SQLite database schema is designed based on the exported CSV files. Each CSV file represents a table in the database, with appropriate primary and foreign keys defined to establish relationships between tables.

### 5. SQLite Database Loading:
Using SQLite, the database schema is created, and the CSV files are loaded into their respective tables. Foreign key constraints are enforced to maintain data integrity and relationships between tables.

### Reasoning for SQLite Database:
SQLite was chosen as the database management system due to its lightweight nature, ease of setup, and compatibility with a wide range of platforms. As this project involves relatively small-scale data processing and analysis, SQLite offers a simple yet efficient solution for storing and querying structured data. Additionally, SQLite's serverless architecture eliminates the need for complex server setups, making it suitable for standalone applications or projects where portability and simplicity are prioritized. Overall, SQLite provides a robust relational database solution that meets the requirements of this project while offering scalability and performance for future expansion if needed.