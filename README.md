# KACE Device Check-in Automator

## Overview
The "kace_device_checkin_automator.py" script automates the process of forcing devices with KACE Agent 9.0+ and greater than 14 days offline to check into the KACE server. It reads device information from a CSV file, pings each device to check its availability, and initiates the inventory update process for devices that respond to the ping.

## Prerequisites
- Python 3.x
- `os` module
- `sys` module
- `csv` module
- `datetime` module
- `getpass` module

## Usage
1. Ensure that Python 3.x is installed on your system.
2. Download or clone the "kace_device_checkin_automator.py" script.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Execute the script by running the following command:
    ```
    python kace_device_checkin_automator.py
    ```
5. Follow the prompts to provide necessary input and allow the script to complete the device check-in process.

## Input
- **CSV File**: The script requires a CSV file containing device information, including hostname or IP address.
- **KACE Server Credentials**: Ensure that the KACE server credentials are properly configured in the script if required for authentication.

## Output
- **Kace_Inv_Log.txt**: The script generates a log file named "Kace_Inv_Log.txt" in the user's Downloads directory. This log file contains detailed information about the device check-in process, including timestamps, ping results, and inventory update actions.

## Notes
- This script utilizes the `ping` command to check the availability of devices. Ensure that the `ping` utility is available and accessible from the command line.
- The script uses `psexec.exe` to remotely execute commands on devices. Make sure that `psexec.exe` is available and properly configured on the system.

## Author
- **Author**: SomeRandomStranger
- **Date**: 7/2/2021

Feel free to modify and customize the script to suit your specific requirements.

