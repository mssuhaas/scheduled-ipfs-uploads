# IPFS Data Uploader 

This project demonstrates how to collect data and upload it to IPFS at scheduled intervals using FastAPI, APScheduler, and Python.

## Features

*   Collects data (simulated or from an external source).
*   Stores data temporarily in memory.
*   Uploads data to IPFS every 10 minutes using a cron-like schedule.
*   Uses APScheduler for reliable scheduling.
*   Built with FastAPI for creating a web API.
*   Handles IPFS interactions with error handling and timeouts.

## Requirements

*   Python 3.10
*   An IPFS node and gateway (or access to a public gateway).

## Installation

1.  Clone the repository:

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Configure the IPFS gateway:

    Create a `.env` file in the root directory and set the `IPFS_GATEWAY` variable:

    ```
    IPFS_GATEWAY=http://your-ipfs-gateway-address:port
    ```
