# Office_Object_detection
A model that detects and identifies office objects.
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

# Dataset
The dataset can be found here: [Link](https://drive.google.com/drive/folders/1CX8gsDy5pCsaMLUwGQ7otMHhz49GK4-L?usp=drive_link)

# Functionalities, Runs and Outputs
<img width="1505" height="1099" alt="image" src="https://github.com/user-attachments/assets/370df537-1b5d-4acc-87c0-ead98f607e11" />

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
## Runs
## Predictions On Images
## Mouse
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/3230a584-f15c-4045-91b0-c49b78f2070d" />

*Detected 1 mouse.*

## Mug
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/1a68e782-e913-45ff-ac4d-b812011a54e9" />

*Detected 1 mug.*

## Pen
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/611af061-0531-4433-a987-77822e74fa8b" />

*Detected 1 pen.*

## Computer
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/d42d5313-f386-429f-8b1a-15693e7fcd66" />

*Detected 1 computer.*

## Keyboard
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/57ba3b7b-83e2-48d3-8d8c-53baab96e236" />

*Detected 1 keyboard.*

## Chair
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/ea576748-510c-4f10-8d42-ac66682e113d" />

*Detected 2 chairs.*

## Book
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/ab46a45b-d2a4-492e-8037-24a8da7c0df6" />

*Detected 1 book.*



# Trouble Shooting
## Problem When Installing Requirements
### Possible Solutions
* Update your python to the 3.13.3 and rerun the pip install.
* If the first point fails, you would have to manually install the following libraries:
    * opencv-python
    * ultralytics
    * pillow
    * Install "[torch v12.9](https://pytorch.org/)" if you would like to train the model on a custom dataset.
## GUI Lag
### Possible Solutions
* Press the "Reset" button.
* Quit program and restart.
