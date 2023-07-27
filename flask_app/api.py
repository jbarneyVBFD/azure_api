from flask import Flask, jsonify
from flask_restful import Api, Resource
import schedule
import time
import numpy as np
import threading

app = Flask(__name__)
api = Api(app)

data = {
    "temperature": None,
    "ph_balance": None,
    "salinity": None,
    "dissolved_oxygen": None
}

# Function to update data
def update_data():
    # Temperature in Fahrenheit, optimal conditions: 50 - 86
    # PH balance optimal conditions: 7 - 9 
    # Salinity optimal between 10 - 30 ppt
    # Dissolved Oxygen optimal above 5 mg/L
    data["temperature"] = np.random.uniform(30.0, 95.0)
    data["ph_balance"] = np.random.uniform(5.0, 11.0)
    data["salinity"] = np.random.uniform(5.0, 35.0)
    data["dissolved_oxygen"] = np.random.uniform(2.0, 10.0)
    
# API Resource
class WaterData(Resource):
    def get(self):
        return jsonify(data)

def job():
    update_data()

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

api.add_resource(WaterData, '/data')

# Schedule the data update every 10 seconds
schedule.every(10).seconds.do(job)

if __name__ == '__main__':
    # Update data once at the start
    update_data()
    
     # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_schedule)
    scheduler_thread.start()

    # Run the Flask app
    app.run(debug=True, port=5001, threaded=True)