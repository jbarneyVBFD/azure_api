import datetime
import logging
import numpy as np
import azure.functions as func

data = {
    "temperature": None,
    "ph_balance": None,
    "salinity": None,
    "dissolved_oxygen": None
}

def update_data():
    # Temperature in Fahrenheit, optimal conditions: 50 - 86
    # PH balance optimal conditions: 7 - 9 
    # Salinity optimal between 10 - 30 ppt
    # Dissolved Oxygen optimal above 5 mg/L
    data["temperature"] = np.random.uniform(30.0, 95.0)
    data["ph_balance"] = np.random.uniform(5.0, 11.0)
    data["salinity"] = np.random.uniform(5.0, 35.0)
    data["dissolved_oxygen"] = np.random.uniform(2.0, 10.0)

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    update_data()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    logging.info('Data updated: %s', data)
