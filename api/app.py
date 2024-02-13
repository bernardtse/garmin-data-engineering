# Import the dependencies.
import numpy as np
import datetime as dt
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template


engine = create_engine("sqlite:///../database/database.sqlite")

app = Flask(__name__)

# Set flag to stop the JSON fields being put in alphabetical order
app.config['JSON_SORT_KEYS'] = False


##################################################################################
# Route to starting page
##################################################################################

@app.route("/")
def home():

    return render_template ("index.html")



##################################################################################
# Routes for the activity types data table
##################################################################################

@app.route("/api/activity-types")
def activitytypes():
    session = Session(engine)
    execute_string = "select * from ActivityTypes"
    activity_types = engine.execute(execute_string).fetchall()
    session.close()

    activity_type_dict = []
    for row in activity_types:
        activity_type = {row[0]:row[1]}
        activity_type_dict.append(activity_type)
        
    return(jsonify(activity_type_dict))


##################################################################################
# Routes for the activities data table
##################################################################################

# return all the data for activities
@app.route("/api/activities/all")
def activities_all():
    session = Session(engine)
    query = "select * from Activities"
    activities = engine.execute(query).fetchall()
    session.close() 
    dict = build_activities_dict(activities)
    return(jsonify(dict))


# return the data for the activity type specified by the end point
@app.route("/api/activities/activity-type/<activity_type_id>")
def activities_by_type(activity_type_id):
    session = Session(engine)
    query = 'SELECT * FROM Activities WHERE "Activity Type ID" = ?'
    activities = engine.execute(query, (activity_type_id,)).fetchall()
    session.close()
    dict = build_activities_dict(activities)
    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("Activity type not found")
    
# return the data for the number of records specified by the end point
@app.route("/api/activities/limit/<number_of_records>")
def activities_by_limit(number_of_records):
    session = Session(engine)
    query = 'SELECT * FROM Activities LIMIT ?'
    activities = engine.execute(query, (number_of_records,)).fetchall()
    session.close()
    dict = build_activities_dict(activities)
    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("Data not found")    

# return the data between the dates specified by the end point
@app.route("/api/activities/date/<start_date>/<end_date>")
def activities_by_date(start_date,end_date):
    if (start_date > end_date):
        return("start date needs to be before the end date")
    else:
        session = Session(engine)
        query = 'SELECT * FROM Activities WHERE Date between ? and ?'
        activities = engine.execute(query, (start_date,end_date)).fetchall()
        session.close()
        dict = build_activities_dict(activities)

    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("No data available for the dates specified")      



##################################################################################
# Routes for the performance metrics data table
##################################################################################
        
# return all the performance data
@app.route("/api/performance-metrics/all")
def performance_metrics_all():
    session = Session(engine)
    query = "select * from PerformanceMetrics"
    perf_metrics = engine.execute(query).fetchall()
    session.close()
    dict = build_perf_metrics_dict(perf_metrics)
    return(jsonify(dict))

# return all the performance data for the activity type specified by the end point
@app.route("/api/performance-metrics/activity-type/<activity_type_id>")
def performance_metrics_by_activity(activity_type_id):
    session = Session(engine)
    query = 'select * from PerformanceMetrics WHERE "Activity Type ID" = ?'
    perf_metrics = engine.execute(query, (activity_type_id,)).fetchall()
    session.close()
    dict = build_perf_metrics_dict(perf_metrics)
    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("Activity type not found")   

# return the performance data for the number of records specified by the end point
@app.route("/api/performance-metrics/limit/<number_of_records>")
def performance_metrics_by_limit(number_of_records):
    session = Session(engine)
    query = 'select * from PerformanceMetrics LIMIT ?'
    perf_metrics = engine.execute(query, (number_of_records,)).fetchall()
    session.close()
    dict = build_perf_metrics_dict(perf_metrics)
    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("Data not found")  


##################################################################################
# Routes for the lap metrics data table
##################################################################################

# return all lap metric data
@app.route("/api/lap-metrics/all")
def lap_metrics():
    session = Session(engine)
    execute_string = "select * from LapMetrics"
    lap_metrics = engine.execute(execute_string).fetchall()
    session.close()       
    dict = build_lap_metrics_dict(lap_metrics)
    return(jsonify(dict))

# return the lap data for the number of records specified by the end point
@app.route("/api/lap-metrics/limit/<number_of_records>")
def lap_metrics_by_limit(number_of_records):
    session = Session(engine)
    query = 'select * from LapMetrics LIMIT ?'
    lap_metrics = engine.execute(query, (number_of_records,)).fetchall()
    session.close()
    dict = build_lap_metrics_dict(lap_metrics)
    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("Data not found")  

##################################################################################
# Routes for the elevation metrics data table
##################################################################################

# return all elevation metric data
@app.route("/api/elevation-metrics/all")
def elevation_metrics():
    session = Session(engine)
    query = "select * from ElevationMetrics"
    elev_metrics = engine.execute(query).fetchall()
    session.close()
    dict = build_elev_metrics_dict(elev_metrics)
    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("Data not found")
    
# return the elevation data for the number of records specified by the end point
@app.route("/api/elev-metrics/limit/<number_of_records>")
def elev_metrics_by_limit(number_of_records):
    session = Session(engine)
    query = 'select * from ElevationMetrics LIMIT ?'
    elev_metrics = engine.execute(query, (number_of_records,)).fetchall()
    session.close()
    dict = build_elev_metrics_dict(elev_metrics)
    if len(dict["data"])>0:
        return(jsonify(dict))
    else:
        return("Data not found")  



##################################################################################
# Functions for building the data dictionaries    
##################################################################################

# Dictionary for the activities table     
##################################################################################
def build_activities_dict(activities):
    activities_dict = {} 
          
    for i in range(0,len(activities)):
          activity = activities[i]
          activities_dict[activity[0]] = ({
                                "ActivityTypeID": activity[1],
                                "Date": activity[2],
                                "Title": activity[3]
                               })         
    meta_dict = {
                "title":"Garmin device - activities",
                "Access time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "Num of records":len(activities_dict),
                "data":{
                        "Activity id":{ "ActivityTypeID":"string",
                                        "Date": "YYYY-MM-DD HH-MM-SS",
                                        "Title": "Activity name"}
                    }
    }
    data_dict = {
                "meta":meta_dict,
                "data":activities_dict
    }  

    return(data_dict)

# Dictionary for the performance metrics table     
##################################################################################
def build_perf_metrics_dict(perf_metrics):
    perf_metrics_dict = {} 
          
    for metric in perf_metrics:
          perf_metrics_dict[metric[0]] = ({
                                "ActivityID": metric[1],
                                "ActivityTypeID":metric[2],
                                "Distance": metric[3],
                                "Calories": metric[4],
                                "Time(mins)": metric[5],
                                "AvgHR":metric[6],
                                "MaxHR":metric[7],
                                "AerobicTE": metric[8],
                                "AvgRunCadence": metric[9],
                                "AvgPace(min/km)": metric[10],
                                "BestPace(min/km)":metric[11]
                               })

    meta_dict = {
                "title":"Garmin device - Performance metrics",
                "Access time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "Num of records":len(perf_metrics_dict),
                "data":{
                    "Performance id":{}
                }
    }
    data_dict = {
                "meta":meta_dict,
                "data":perf_metrics_dict
    } 
    return(data_dict)

# Dictionary for the lap metrics table     
##################################################################################
def build_lap_metrics_dict(lap_metrics):
          
    lap_metrics_dict = {} 
          
    for metric in lap_metrics:
          lap_metrics_dict[metric[0]] = ({
                                "ActivityID": metric[1],
                                "BestLapTime(min)":metric[2],
                                "NumberofLaps": metric[3],
                                "TotalDistance(km)": metric[4],
                                "LapDistance(km)": round(metric[5],3),
                                "MovingTime(min)":metric[6],
                                "ElapsedTime(min)":metric[7]
                               })
    meta_dict = {
                "title":"Garmin device - Lap metrics",
                "Access time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "Num of records":len(lap_metrics_dict),
                "data":{
                    "Lap id":{}
                }
    }   
    data_dict = {
                "meta":meta_dict,
                "data":lap_metrics_dict
    }
    return(data_dict)

# Dictionary for the elevation metrics table     
##################################################################################
def build_elev_metrics_dict(elev_metrics):

    elev_metrics_dict = {} 
          
    for metric in elev_metrics:
        elev_metrics_dict[metric[0]] = ({
                                "ActivityID": metric[1],
                                "TotalAscent":metric[2],
                                "TotalDescent": metric[3],
                                "MinElevation": metric[4],
                                "MaxElevation": metric[5],
                               })
    meta_dict = {
                "title":"Garmin device - Elevation metrics",
                "Access time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "Num of records":len(elev_metrics_dict),
                "data":{
                    "Elevation id":{}
                }
    }
    data_dict = {
                "meta":meta_dict,
                "data":elev_metrics_dict
    }
    
    return(data_dict)

    
##################################################################################
if __name__ == '__main__':
    app.run(debug=False)
