import datetime
import logging
import numpy as np
import azure.functions as func
from azure.data.tables import TableClient, TableEntity
from decouple import config

account_name = config('AZURE_STORAGE_ACCOUNT_NAME')
account_key = config('AZURE_STORAGE_ACCOUNT_KEY')
table_endpoint = config('AZURE_STORAGE_TABLE_ENDPOINT')

connection_string = (f"DefaultEndpointsProtocol=https;"
                         f"AccountName={account_name};"
                         f"AccountKey={account_key};"
                         f"TableEndpoint={table_endpoint};")

table_client = TableClient.from_connection_string(connection_string, table_name="SensorData")

logging.basicConfig(level=logging.INFO)

data = {
    "temperature": None,
    "ph_balance": None,
    "salinity": None,
    "dissolved_oxygen": None
}

def update_data():
    try:
        # Temperature in Fahrenheit, optimal conditions: 50 - 86
        data["temperature"] = np.random.uniform(30.0, 95.0)
        if not 50 <= data["temperature"] <= 86:
            logging.warning("Temperature is out of optimal conditions.")

        # PH balance optimal conditions: 7 - 9 
        data["ph_balance"] = np.random.uniform(5.0, 11.0)
        if not 7 <= data["ph_balance"] <= 9:
            logging.warning("PH balance is out of optimal conditions.")

        # Salinity optimal between 10 - 30 ppt
        data["salinity"] = np.random.uniform(5.0, 35.0)
        if not 10 <= data["salinity"] <= 30:
            logging.warning("Salinity is out of optimal conditions.")

        # Dissolved Oxygen optimal above 5 mg/L
        data["dissolved_oxygen"] = np.random.uniform(2.0, 10.0)
        if data["dissolved_oxygen"] <= 5:
            logging.warning("Dissolved Oxygen is below optimal conditions.")

        logging.info("Data updated successfully.")
        return data

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    updated_data = update_data()

    # Store data in Azure Table Storage
    data_entity = TableEntity(
        PartitionKey='SensorReadings',
        RowKey=utc_timestamp,  # Using the timestamp as RowKey to ensure uniqueness
        Temperature=updated_data["temperature"],
        PHBalance=updated_data["ph_balance"],
        Salinity=updated_data["salinity"],
        DissolvedOxygen=updated_data["dissolved_oxygen"]
    )
    table_client.create_entity(entity=data_entity)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    logging.info('Data updated: %s', updated_data)