CREATE TABLE ActivityTypes (
    ActivityTypeID TEXT PRIMARY KEY,
    ActivityType TEXT
);

CREATE TABLE Activities (
    ActivityID INTEGER PRIMARY KEY,
    ActivityTypeID TEXT,
    Date DATETIME,
    Title TEXT,
    FOREIGN KEY (ActivityTypeID) REFERENCES ActivityTypes(ActivityTypeID)
);

CREATE TABLE PerformanceMetrics (
    PerformanceID TEXT PRIMARY KEY,
    ActivityID INTEGER,
    ActivityTypeID TEXT,
    Distance FLOAT,
    Calories FLOAT,
    TimeMinutes FLOAT,
    AvgHR INTEGER,
    MaxHR INTEGER,
    AerobicTE FLOAT,
    AvgRunCadence FLOAT,
    AvgPaceMinKm FLOAT,
    BestPaceMinKm FLOAT,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID),
    FOREIGN KEY (ActivityTypeID) REFERENCES ActivityTypes(ActivityTypeID)
);

CREATE TABLE LapMetrics (
    LapID TEXT PRIMARY KEY,
    ActivityID INTEGER,
    BestLapTimeMin FLOAT,
    NumberOfLaps INTEGER,
    TotalDistanceKm FLOAT,
    LapDistanceKm FLOAT,
    MovingTimeMin FLOAT,
    ElapsedTimeMin FLOAT,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID)
);

CREATE TABLE ElevationMetrics (
    ElevationMetricID TEXT PRIMARY KEY,
    ActivityID INTEGER,
    TotalAscent INTEGER,
    TotalDescent INTEGER,
    MinElevation INTEGER,
    MaxElevation INTEGER,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID)
);
