# Office_Object_detection
A model that detects and identifies office objects
# Installation Guide
## What You Need
* [Visual studio code](https://code.visualstudio.com/) or [Pycharm](https://www.jetbrains.com/pycharm/download/)
* Python 3.13.3. Link: https://www.python.org/downloads/
### Step 1: Get the code
The fastest way to get started is to fork the project and initiate a pull request using git.
```git
git pull https://github.com/theoldonee/Office_Object_detection.git
```
### Step 2: Install libraries
In the IDE terminal, run:
```bash
pip install -r requirements.txt
```
### Step 3: Run the program
Simply press the play button while on the main.py file or in the terminal, run:
```bash
python main.py
```
# Classes
Th current model is trained on the following classes.

<img width="473" height="271" alt="image" src="https://github.com/user-attachments/assets/ed3015f3-b2e0-47ab-bcdf-9f4b415946fe" />

# Functionalities, Runs and Outputs
The following are the variety of actions that can be performed once the program is ran.
## Functionalities
### Reset GUI
Pressing the "back" button retuns the gui to its default state.
### Image Upload
Pressing the "Upload Image" button gives the user the option to upload an image file and have a prediction made on the image.
### Live Capture
Pressing the "Capture" button captures the current video frame and performs a prediction on it.
### Live Detection
Pressing the "Start Live Detection" button gives the user the option to make prediction on the live feed.
### Quit
On pressing the "Quit" button, the program is terminated.
# Trouble Shooting
## Problem When Installing Requirements.
### Possible Solutions
* Update your python to the 3.13.3 and rerun the pip install
* If the first point fails, you would have to manually install the following libraries
    * opencv-python
    * ultralytics
    * pillow
    * Install "[torch v12.9](https://pytorch.org/)" if you would like to train the model on a custom dataset.
