# Garmin Data Engineering

---

## Project Overview

This project aims to develop a comprehensive data engineering solution to analyze exercise and fitness patterns captured through Garmin wearable devices. By leveraging data collected from an individual's Garmin watch, with explicit consent and a focus on privacy, we aim to transform this rich dataset into a structured database. This enables us to explore fitness trends, understand exercise habits across different ages and regions, and potentially improve personal health and fitness strategies.

Our motivation is rooted in the belief that well-structured and accessible data can unlock insights into exercise behaviors, aiding individuals and researchers in making informed decisions about physical activity. With a commitment to privacy and ethical data use, this project serves as a foundation for scalable data-driven analysis in the realm of personal fitness.

### Contents
- [Key Features](#Key-Features)
- [Technical Stack](#Technical-Stack)
- [Getting Started](#Getting-Started)
- [Usage](#Usage)
- [Documentation](#Documentation)
- [Ethical Considerations](#Ethical-Considerations)
- [References](#References)
- [Acknowledgments](#Acknowledgments)
- [Collaborators](#Collaborators)

### <a id="Key-Features"></a>Key Features

- **ETL Workflow**: Implements a robust Extract, Transform, Load (ETL) process to ingest and refine fitness activity data.
- **Database Design**: Utilizes a relational database structure with multiple tables to organize data efficiently, allowing for scalability and complex queries.
- **Data Analysis Tools**: Includes methods for reading data from the database, enabling analysis and visualization through Pandas DataFrames and a Flask API for broader access.
- **Privacy and Ethics**: Adheres to strict privacy guidelines, ensuring no personally identifiable information (PII) is stored or analyzed.

### <a id="Technical-Stack"></a>Technical Stack

- **SQLite**: Chosen for its lightweight nature and ease of integration with Python, ideal for this project's scale and objectives.
- **Pandas**: For data manipulation and transformation during the ETL process.
- **Flask**: To provide an API interface for accessing and interacting with the stored data.

### <a id="Getting-Started"></a>Getting Started

To get started with this project, clone the repository and install the required Python packages listed in [`requirements.txt`](requirements.txt). Ensure you have Python 3.2 installed on your system.

```bash
git clone https://github.com/NidaB-C/garmin-data-engineering
cd garmin-data-engineering
pip install -r requirements.txt
```

Follow the instructions in the [`setup.md`](setup.md) document to initialize the database and start the Flask API server.

### <a id="Usage"></a>Usage

- **ETL Process**: Run the ETL scripts to extract data from the CSV, transform it according to the project schema, and load it into the SQLite database.
- **API Access**: Use the Flask API endpoints to query the database and retrieve JSON-formatted data for analysis or application integration.

### <a id="Documentation"></a>Documentation

- **ETL Workflow**: Detailed documentation of the ETL process, including data transformation rules and loading strategies, is available in [`docs/etl_workflow.md`](docs/etl_workflow.md).
- **Database Schema**: The database design, including table structures and relationships, is described in [`docs/db_design.md`](docs/db_design.md). An Entity-Relationship Diagram (ERD) is also provided for visual reference.
- **API Guide**: Instructions on utilizing the Flask API, including endpoint descriptions and example requests, can be found in [`docs/api_usage.md`](docs/api_usage.md).

### <a id="Ethical-Considerations"></a>Ethical Considerations

We are committed to maintaining the highest standards of privacy and ethics. The data used in this project has been provided with informed consent, strictly for non-commercial purposes. All analysis is conducted in a manner that ensures individuals' anonymity, with no PII being collected, stored, or analyzed. This project's design facilitates the addition of data from other individuals under similar ethical guidelines, aiming to enrich our understanding of fitness patterns while upholding our commitment to privacy and data protection.


### <a id="References"></a>References

- **Data Source**: Garmin Connect (Data provided by an individual under consent)
- **Python Libraries**: Pandas, SQLite3, Flask, nbconvert

### <a id="Acknowledgments"></a>Acknowledgments

We would like to thank all contributors and participants who have made this project possible. Special thanks to the individual who provided their fitness data, enabling this exploration into exercise and health analytics.

### <a id="Collaborators"></a>Collaborators

* [Aysha Gheewala](https://github.com/AyshaGheewala)
* [Mohammad Nawaz](https://github.com/MoNawaz101)
* [Sum Yeung Bernard Tse](https://github.com/bernardtse)
* [Nida Ballinger-Chaudhary](https://github.com/NidaB-C)
