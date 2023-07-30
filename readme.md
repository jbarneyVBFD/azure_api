# Azure API for Generating Sensor Readings

This repository contains an Azure Function that provides an API for sensor data. This data is intended to be used with the SCADA Power Apps project.

## Overview

The Azure Function fetches sensor data, which includes metrics like temperature, pH balance, salinity, and dissolved oxygen. This data is crucial for monitoring and ensuring the optimal operation of the SCADA system.

## Prerequisites

- Azure account with an active subscription.
- Python 3.x
- Azure Functions Core Tools
- Azure CLI (optional)

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/jbarneyVBFD/azure_api
    cd azure_api

2. **Set up a Virtual Environment (optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt

4. **Local Development**

To run the function locally:
    ```bash
    func start

## Deployment to Azure

1. **Login to Azure**

    ```bash
    az login

2. **Deploy the Function**

Follow the Azure Functions deployment guide to deploy this function to your Azure account.

## Usage

Once deployed, the function can be triggered to generate the latest sensor data. This data can then be consumed by the SCADA Power Apps project.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or concerns, please open an issue or contact the repository owner.