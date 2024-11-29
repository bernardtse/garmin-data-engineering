# Garmin Data Engineering

![Garmin Data Engineering](images/banner.png)


## Contents
1. [Project Overview](#1-project-overview)
2. [Key Features](#2-key-features)
3. [Technical Stack](#3-technical-stack)
4. [Getting Started](#4-getting-started)
5. [Usage](#5-usage)
6. [Documentation](#6-documentation)
7. [Ethical Considerations](#7-ethical-considerations)
8. [References](#8-references)
9. [Acknowledgments](#9-acknowledgments)
10. [Collaborators](#10-collaborators)

## 1. Project Overview

This project aims to develop a comprehensive data engineering solution to analyse exercise and fitness patterns captured through Garmin wearable devices. By leveraging data collected from an individual's Garmin watch, with explicit consent and a focus on privacy, we aim to transform this rich dataset into a structured database. Through additional visualisation efforts by application or web developers, individuals have the opportunity to track and enhance their personal health and fitness strategies.

Our motivation is rooted in the belief that well-structured and accessible data can unlock insights into exercise behaviours, aiding individuals and researchers in making informed decisions about physical activity. With a commitment to privacy and ethical data use, this project serves as a foundation for scalable data-driven analysis in the realm of personal fitness.

## 2. Key Features

- **ETL Workflow**: Implements a robust Extract, Transform, Load (ETL) process to ingest and refine fitness activity data.
- **Database Design**: Utilises a relational database structure with multiple tables to organise data efficiently, allowing for scalability and complex queries.
- **Data Analysis Tools**: Includes methods for reading data from the database, enabling analysis and visualisation through Pandas DataFrames and a Flask API for broader access.
- **Privacy and Ethics**: Adheres to strict privacy guidelines, ensuring no personally identifiable information (PII) is stored or analysed.

## 3. Technical Stack

- **SQLite**: Chosen for its lightweight nature and ease of integration with Python, ideal for this project's scale and objectives.
- **Pandas**: For data manipulation and transformation during the ETL process.
- **Flask**: To provide an API interface for accessing and interacting with the stored data.

## 4. Getting Started

To get started with this project, clone the repository and install the required Python packages listed in [`requirements.txt`](requirements.txt). Ensure you have Python 3 installed on your system.

Original Project
```bash
git clone https://github.com/NidaB-C/garmin-data-engineering.git
cd garmin-data-engineering
pip install -r requirements.txt
```
Forked Project
```bash
git clone https://github.com/bernardtse/garmin-data-engineering.git
cd garmin-data-engineering
pip install -r requirements.txt
```

Follow the instructions in the [`SETUP.md`](SETUP.md) document to initialise the database and start the Flask API server.

## 5. Usage

- **ETL Process**: Run the ETL scripts to extract data from the CSV, transform it according to the project schema, and load it into the SQLite database.
- **API Access**: Use the Flask API endpoints to query the database and retrieve JSON-formatted data for analysis or application integration.

![API](images/api.png)

## 6. Documentation

- **ETL Workflow**: Detailed documentation of the ETL process, including data transformation rules and loading strategies, is available in [`docs/ETL_WORKFLOW.md`](docs/ETL_WORKFLOW.md).
- **Database Schema**: The database design, including table structures and relationships, is described in [`docs/DB_DESIGN.md`](docs/DB_DESIGN.md). An Entity-Relationship Diagram (ERD) is also provided for visual reference.
- **API Guide**: Instructions on utilising the Flask API, including endpoint descriptions and example requests, can be found in [`docs/API_USAGE.md`](docs/API_USAGE.md).

## 7. Ethical Considerations

We are committed to maintaining the highest standards of privacy and ethics. The data used in this project has been provided with informed consent, strictly for non-commercial purposes. All analysis is conducted in a manner that ensures individuals' anonymity, with no PII being collected, stored, or analysed. This project's design facilitates the addition of data from other individuals under similar ethical guidelines, aiming to enrich our understanding of fitness patterns while upholding our commitment to privacy and data protection.


## 8. References

- **Data Source**: Garmin Connect (Data provided by an individual under consent)
- **Python Libraries**: Pandas, SQLite3, Flask, nbconvert

## 9. Acknowledgments

We would like to thank all contributors and participants who have made this project possible. Special thanks to the individual who provided their fitness data, enabling this exploration into exercise and health analytics.

## 10. Collaborators

- [Aysha Gheewala](https://github.com/AyshaGheewala)
- [Mohammed Nawaz](https://github.com/MoNawaz101)
- [Sum Yeung Bernard Tse](https://github.com/bernardtse)
- [Nida Ballinger-Chaudhary](https://github.com/NidaB-C)
