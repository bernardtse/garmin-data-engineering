# Import the dependencies.
import numpy as np
import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import desc

from flask import Flask, jsonify


engine = create_engine("sqlite:///../database/database.sqlite")

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def welcome():

    """List all available api routes."""
    return (
            f"Available Routes:<br/><br/>"
            f"/api/ActivityTypes<br/><br/>"
            f"/api/Activities<br/><br/>"
            f"/api/PerformanceMetrics<br/><br/>"
            f"/api/LapMetrics<br/><br/>"
            f"/api/ElevationMetrics<br/><br/>"
            )   




@app.route("/api/ActivityTypes")
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

@app.route("/api/Activities")
def activities():
    session = Session(engine)
    execute_string = "select * from Activities"
    activities = engine.execute(execute_string).fetchall()
    session.close()

    activities_dict = {} 
          
    for i in range(0,len(activities)):
          activity = activities[i]
          activities_dict[activity[0]] = ({
                                "ActivityTypeID": activity[1],
                                "Date": activity[2],
                                "Title": activity[3]
                               })         
    return(jsonify(activities_dict))

@app.route("/api/PerformanceMetrics")
def performancemetrics():
    session = Session(engine)
    execute_string = "select * from PerformanceMetrics"
    perf_metrics = engine.execute(execute_string).fetchall()
    session.close()

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
          
    return(jsonify(perf_metrics_dict))

@app.route("/api/LapMetrics")
def lapmetrics():
    session = Session(engine)
    execute_string = "select * from LapMetrics"
    lap_metrics = engine.execute(execute_string).fetchall()
    session.close()

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
          
    return(jsonify(lap_metrics_dict))

@app.route("/api/ElevationMetrics")
def elevationmetrics():
    session = Session(engine)
    execute_string = "select * from ElevationMetrics"
    elevation_metrics = engine.execute(execute_string).fetchall()
    session.close()

    elev_metrics_dict = {} 
          
    for metric in elevation_metrics:
          elev_metrics_dict[metric[0]] = ({
                                "ActivityID": metric[1],
                                "TotalAscent":metric[2],
                                "TotalDescent": metric[3],
                                "MinElevation": metric[4],
                                "MaxElevation": metric[5],
                               })
          
    return(jsonify(elev_metrics_dict))


if __name__ == '__main__':
    app.run(debug=True)
