Screenshot Script
This script takes a screenshot after a 5-second delay and saves it to a specified directory with a unique filename based on the current timestamp.

Requirements
Python 3.x
pyautogui library
pathlib library
Installation
Install Python 3.x from python.org.

Install the required libraries using pip:

bash
Copy code
pip install pyautogui
Usage
Save the script to a file, e.g., screenshot.py.

Run the script from the command line:

bash
Copy code
python screenshot.py
The script will wait for 5 seconds before taking a screenshot. This gives you time to set up the screen as desired.

The screenshot will be saved in the screenshot_data directory under your user's home directory. The filename will be a unique timestamp in milliseconds.

The screenshot will also be displayed using the default image viewer.


Notes
Ensure that you have the necessary permissions to create directories and save files in the specified location.
You can change the save location by modifying the directory variable in the script.
Troubleshooting
If you encounter an error, ensure that all required libraries are installed and that you have the necessary permissions.
Refer to the error message for specific details on what went wrong.
