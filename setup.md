## Setup Instructions for Garmin Data Engineering Project

This document provides detailed instructions on setting up the project environment, initializing the database, and starting the Flask API server.

### Prerequisites

Before starting, ensure you have the following installed on your system:
- Python 3.2
- pip (Python package manager)

### Step 1: Clone the Repository

Clone the repository to your local machine by running the following command in your terminal:

```bash
git clone https://github.com/NidaB-C/garmin-data-engineering.git
cd garmin-data-engineering
```

### Step 2: Create a Conda Environment 

Create a new Conda environment for the project dependencies. Run the following command:

```bash
conda create --name dev python=3.2
```
### Step 3: Activate the Conda Environment:

Activate the newly created Conda environment by running:

```bash
conda activate dev
```

### Step 4: Install Dependencies

Install the project dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Step 5: Initialize the Database 

Run the ETL scripts to extract data from the CSV files, transform the data, and load it into the SQLite database. Execute the following commands:

```bash
python etl/load.py
python etl/transform.py
```
These scripts will create an SQLite database in the `database` directory with the necessary tables and data.

### Step 6: Start the Flask API Server 

Navigate to the api directory and run the Flask application with the following command:

```bash
cd api
python app.py
```
The Flask API server will start, and you should see output indicating that the server is running, typically on [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/).

### Accessing the API

With the server running, you can access the API endpoints using a web browser or tools like curl or Postman. For example, to access the root endpoint:

```bash
Copy code
curl http://127.0.0.1:5000/
```
Refer to the [`API documentation`](docs/api_usage.md) for more information on available endpoints and their usage.

### Conclusion
You have successfully set up the Garmin Data Engineering project environment, initialized the database, and started the Flask API server. Explore the API endpoints to interact with the activity metrics data.