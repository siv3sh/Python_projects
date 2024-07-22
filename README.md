# Screenshot Script with GUI

This script takes a screenshot after a 5-second delay and saves it to a specified directory with a unique filename based on the current timestamp. A graphical user interface (GUI) is provided using `tkinter` to allow users to trigger the screenshot and quit the application via buttons.

## Requirements

- Python 3.x
- `pyautogui` library
- `pathlib` library
- `tkinter` (usually comes pre-installed with Python)

## Installation

1. **Install Python 3.x** from [python.org](https://www.python.org/).

2. **Install the required libraries** using pip:

    ```bash
    pip install pyautogui
    ```

## Usage

1. **Save the script** to a file, e.g., `screenshot_gui.py`.

2. **Run the script** from the command line:

    ```bash
    python screenshot_gui.py
    ```

3. The GUI will appear with two buttons:
   - **"Take Screenshot"**: Takes a screenshot after a 5-second delay and saves it to the `screenshot_data` directory under your user's home directory with a unique timestamp-based filename.
   - **"Quit"**: Closes the application.

4. The screenshot will be saved in the `screenshot_data` directory and displayed using the default image viewer.

## Configuration

- **Save Location**: The screenshots are saved in the `screenshot_data` directory under your user’s home directory. You can change the save location by modifying the `directory` variable in the script.

## Notes

- Ensure you have the necessary permissions to create directories and save files in the specified location.
- If the GUI does not display correctly, ensure that `tkinter` is properly installed and check for any GUI-related issues on your platform.

## Troubleshooting

- **Library Installation Errors**: Ensure that all required libraries (`pyautogui`, `tkinter`) are installed. Use `pip install <library>` to install any missing libraries.
- **Permission Issues**: Ensure you have write permissions to the directory where the screenshots are being saved.
- **Error Messages**: Refer to the error messages for specific details on what went wrong and adjust the script or environment as needed.

## License

This script is provided for educational purposes and personal use. Modify and distribute as needed, but ensure you comply with any relevant licenses for the libraries used.
