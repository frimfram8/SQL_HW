# import all the things
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurements = Base.classes.measurements

# Create our session (link) from Python to the DB
session = Session(engine)

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Query for the date and temperature observations (tobs) from the last year in measurements table
# Convert the query results to a Dictionary using `date` as the key and `tobs` as the value
# Return the json representation of your dictionary
@app.route("/api/v1.0/temp")
def dateTobs():
      # Query all data from Measurements table
    results = session.query(Measurements).all()

    # Create a dictionary from the row data and append to a list of date_and_temp
    date_and_temp = []
    for result in results:
        tobs_dict = {}
        tobs_dict["date"] = Measurements.date #how to filter date??
        tobs_dict["temp"] = Measurements.tobs
        date_and_temp.append(tobs_dict)

    return jsonify(date_and_temp)

# Return a json list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations():
      # Query station column from Measurements table
    results = session.query(Measurements.station).all()

    return jsonify(results)


# Return a json list of Temperature Observations (tobs) for the previous year
@app.route("/api/v1.0/tobs")
def tobs():
      # Query all data from Measurements table
    results = session.query(Measurements.tobs).all()

    return jsonify(results)



# Return a json list of the minimum temperature, the average temperature, and the max temperature 
# for a given start or start-end range.

# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than 
# and equal to the start date.
@app.route("/api/v1.0/<start>")
def start_search(start):
    split_date = start.split("-")
    #look into strptime 

    # Query all data from Measurements table
    results = session.query(Measurements).all()

    dict = {}
    
    for result in results:
        if Measurements.date is >= start ????
        dict["date"] = Measurements.date
        dict["temp"] = Measurements.tobs
        dict.append(tobs_dict)

    return jsonify(dict)
    TMIN = dict.value.minimum
    TAVG = dict.value.average
    TMAX = dict.value.max

    print(f"The minimum temp is {TMIN}, the average temp is {TAVG}, and the maximum temp is {TMAX}.")


   
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between 
# the start and end date inclusive
 #/api/v1.0/<start>/<end>

if __name__ == "__main__":
    app.run(debug=True)
