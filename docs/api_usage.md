# API Usage Documentation

Welcome to our API documentation. This API provides access to a wealth of information regarding activity tracking, including types of activities, individual activities, performance metrics, lap data, and elevation data during activities. Our API endpoints are designed to deliver comprehensive data in an easily consumable JSON format.

## Available Endpoints

### Activity Types

- **GET `/api/activity-types`**
  - Description: Retrieve information on the various types of activities.

### Activities

- **GET `/api/activities/all`**
  - Description: Fetch details on all activities undertaken.
  
- **GET `/api/activities/activity-type/{ActivityTypeID}`**
  - Description: Obtain activities filtered by a specific activity type.
  - Parameters:
    - `ActivityTypeID`: The ID representing the type of activity.

- **GET `/api/activities/limit/{number_of_records}`**
  - Description: Retrieve a limited number of activity records.
  - Parameters:
    - `number_of_records`: The maximum number of records to return.

- **GET `/api/activities/date/{start_date}/{end_date}`**
  - Description: Get activities within a specified date range.
  - Parameters:
    - `start_date`: The start date in the format YYYY-MM-DD.
    - `end_date`: The end date in the format YYYY-MM-DD.

### Performance Metrics

- **GET `/api/performance-metrics/all`**
  - Description: Access all data on performance metrics during activities.

- **GET `/api/performance-metrics/activity-type/{activity_type_id}`**
  - Description: Fetch performance metrics filtered by activity type.
  - Parameters:
    - `activity_type_id`: The ID of the activity type.

- **GET `/api/performance-metrics/limit/{number_of_records}`**
  - Description: Limit the number of performance metrics records returned.
  - Parameters:
    - `number_of_records`: The maximum number of records to fetch.

### Lap Metrics

- **GET `/api/lap-metrics/all`**
  - Description: Retrieve all lap data during running activities.

- **GET `/api/lap-metrics/limit/{number_of_records}`**
  - Description: Obtain a limited number of lap metrics records.
  - Parameters:
    - `number_of_records`: The maximum number of records to return.

### Elevation Metrics

- **GET `/api/elevation-metrics/all`**
  - Description: Access all elevation data during running activities.

- **GET `/api/elev-metrics/limit/{number_of_records}`**
  - Description: Fetch a limited number of elevation metrics records.
  - Parameters:
    - `number_of_records`: The maximum number of records to retrieve.

## Usage Notes

- Replace placeholders in curly braces {} with actual values.
- The date format for endpoints involving dates is **YYYY-MM-DD**.
- Responses are structured to include metadata for informational purposes and a data array containing the requested records.

## JSON Response Structure

The JSON response from each endpoint includes both metadata and data sections:

```json
{
  "meta": {
    "title": "Garmin device - activities",
    "Access time": "11/02/2024 19:55:58",
    "Num of records": 413
  },
  "data": {
    "1": {
      "ActivityTypeID": "AT001",
      "Date": "2024-01-22 20:19:55",
      "Title": "Treadmill Running"
    },
    "2": {
      "ActivityTypeID": "AT001",
      "Date": "2024-01-18 17:02:50",
      "Title": "Treadmill Running"
    },
    "3": {
      "ActivityTypeID": "AT001",
      "Date": "2024-01-15 19:33:44",
      "Title": "Treadmill Running"
    },
    // Additional records...
  }
}

