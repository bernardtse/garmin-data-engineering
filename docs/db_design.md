## Database Design Overview

The database design for this project is designed to efficiently store and manage data related to activity tracking sessions. The design includes several tables representing different entities, such as activities, activity types, performance metrics, lap metrics, and elevation metrics. These tables are interconnected through primary and foreign key relationships to maintain data integrity and facilitate data analysis.

---

## Table Structures and Relationships

1. **Activities Table**:
   - **Attributes**: ActivityID (Primary Key), ActivityTypeID (Foreign Key), Date, Title
   - **Description**: Stores basic details about each activity, such as its unique identifier, activity type, date, and title.
   - **Relationships**: Connected to the ActivityTypes table through the ActivityTypeID foreign key.

2. **ActivityTypes Table**:
   - **Attributes**: ActivityTypeID (Primary Key), ActivityType
   - **Description**: Contains a list of activity types along with their unique identifiers.
   - **Relationships**: Connected to the Activities table through the ActivityTypeID foreign key.

3. **PerformanceMetrics Table**:
   - **Attributes**: PerformanceID (Primary Key), ActivityID (Foreign Key), Distance, Calories, Time (minutes), AvgHR, MaxHR, AerobicTE, AvgRunCadence, AvgPace (min/km), BestPace (min/km)
   - **Description**: Stores specific performance metrics for each activity, including distance covered, calories burned, time duration, heart rate metrics, and pace information.
   - **Relationships**: Connected to the Activities table through the ActivityID foreign key.

4. **LapMetrics Table**:
   - **Attributes**: LapID (Primary Key), ActivityID (Foreign Key), BestLapTime (min), NumberOfLaps, TotalDistance (km), LapDistance (km), MovingTime (min), ElapsedTime (min)
   - **Description**: Captures lap-specific metrics for activities involving multiple laps, including lap times, total distance covered, and time metrics.
   - **Relationships**: Connected to the Activities table through the ActivityID foreign key.

5. **ElevationMetrics Table**:
   - **Attributes**: ElevationMetricID (Primary Key), ActivityID (Foreign Key), TotalAscent, TotalDescent, MinElevation, MaxElevation
   - **Description**: Records elevation-related metrics for each activity, such as total ascent, total descent, and minimum/maximum elevation.
   - **Relationships**: Connected to the Activities table through the ActivityID foreign key.

![ERD](erd.png)

## Database Integrity Constraints

- **Primary Keys**: Each table has a primary key constraint to ensure uniqueness and identify each record uniquely.
- **Foreign Keys**: Foreign key constraints establish relationships between tables, ensuring referential integrity and enforcing data consistency.
- **Unique Constraints**: Certain attributes, such as ActivityTypeID and ActivityType in the ActivityTypes table, have unique constraints to prevent duplicate entries.

---

*This database design facilitates efficient data storage, retrieval, and analysis of activity tracking data. The interconnected tables and relationships enable comprehensive data exploration and insights into various aspects of activity performance.*


