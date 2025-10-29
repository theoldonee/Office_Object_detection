from time import sleep
import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
import cv2
from .button import GUIButton
from ..object_detection.detector import Detector

class GUI:
    def __init__(self, root):
        # initialising main window
        self.root = root
        self.root.title("Office Object Detection") # title
        self.root.geometry("900x700+700+300") # set size and location
        self.detector = Detector()
        self.predict = False


        # setting up the layout
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # left section: for image/webcam display
        self.left_frame = tk.Frame(main_frame, width=625, height=625)
        self.left_frame.pack(side="left", anchor="n")
        self.image_label = tk.Label(self.left_frame)
        self.image_label.pack()
        self.original_img = None

        # right section: button panel
        right_frame = tk.Frame(main_frame, width=300)
        right_frame.pack(side="right", fill="y")

        #header label
        header = Label(right_frame, text="Office Object Detection", fg="black", font=("Helvetica", 15))
        header.pack(pady=(30, 20))

        # upload image button
        upload_img_btn = GUIButton(right_frame, text="Upload Image", command=self.upload_image, font=("Helvetica", 12))
        upload_img_btn.pack(pady=10)
        upload_img_btn.config_colours(activeBG="green4", activeFG="white", bgcolour="SpringGreen3",
                                      fgcolour="white", hoverBG="green3", hoverFG="white")

        #capture frame button
        capture_btn = GUIButton(right_frame, text="Capture", command=self.capture_frame, font=("Helvetica", 12))
        capture_btn.pack(pady=10)
        capture_btn.config_colours(activeBG="dodgerblue4", activeFG="white",  bgcolour="dodgerblue3", fgcolour="white", hoverBG="dodgerblue2", hoverFG="white")

        #start live detection button
        live_stream_btn = GUIButton(right_frame, text="Live Detection", command=self.start_prediction, font=("Helvetica", 12))
        live_stream_btn.pack(pady=10)
        live_stream_btn.config_colours(activeBG="green4", activeFG="white",
                                       bgcolour="SpringGreen3", fgcolour="white", hoverBG="green3", hoverFG="white")

        # back button (returns to default livestream)
        back_btn = GUIButton(right_frame, text="Back",command=self.go_back,font =("Helvetica", 12))
        back_btn.pack(pady=10)
        back_btn.config_colours(activeBG="gray30", activeFG="white", bgcolour="gray60",
                                fgcolour="white",hoverBG="gray40", hoverFG="white")

        #quit button (ends program)
        quit_btn = GUIButton(right_frame, text="Quit",command=self.quit_app,  font=("Helvetica", 12))
        quit_btn.pack(pady=10)
        quit_btn.config_colours(activeBG="firebrick4", activeFG="white", bgcolour="firebrick3",
                                fgcolour="white", hoverBG="red", hoverFG="white")

        quit_btn.set_dimensions(height=2, width=8)

        # cv2 webcam state
        self.cap = None
        self.running = False

        # starts live detection by default
        self.start_video_stream()

    # method to upload an image file
    def upload_image(self):
        # Stop webcam if it is running
        self.stop_video_stream()
        # open file dialogue
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if filename:
            self.display_image(filename) # display selected image

    #method to display the uploaded image file on the left section
    def display_image(self, path):
        self.stop_video_stream()  # to ensure the live stream is stopped
        self.original_img = Image.open(path) # loads image from file
        imgtk = ImageTk.PhotoImage(self.original_img) # converts to Tkinter-compatible format
        self.image_label.imgtk = imgtk  # this prevents garbage collection
        self.image_label.configure(image=imgtk) # displays image in label
        self.resize_display(imgtk.width(), imgtk.height()) # rezises and centres window

    #method to start and continue webcam feed
    def start_video_stream(self):
        if not self.running:
            self.cap = cv2.VideoCapture(0) # open default webcam
            self.running = True # mark webcam feed as active
            self.update_video() # update the frames

    # method to end webcam feed
    def stop_video_stream(self):
        self.running = False # ends the update loop
        if self.cap:
            self.cap.release() # release the webcam
            self.cap = None #resets the capture object
        self.image_label.config(image='') # clear the display area

    # method to update webcam feed
    def update_video(self):
        if self.running and self.cap:
            ret, frame = self.cap.read() # reads frame from the webcam
            if ret:
                # checks if prediction should be made
                if self.predict:
                    imgtk = self.predict_frame(frame, True)
                else:
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # converts BGR to RGB
                    img = Image.fromarray(rgb_frame).resize((625, 625)) # comverts to PIL image and resize
                    imgtk = ImageTk.PhotoImage(image=img) # converts to Tkinter-compatible format
                self.image_label.imgtk = imgtk # this prevents garbage collection
                self.image_label.configure(image=imgtk) # display the image
            self.root.after(50, self.update_video) # schedules a new frame every 50 ms

    # method to quit app
    def quit_app(self):
        self.stop_video_stream() # stop video stream if it's on
        self.root.quit() # exit gui

    # method to reset the layout to the default state (live detection)
    def go_back(self):
        self.stop_video_stream() # stops any active video stream
        self.image_label.config(image='') # clear image
        self.image_label.imgtk = None # remove reference to the mage object
        self.original_img = None # reset to uploaded image state
        self.resize_display(600, 600) # return to default display size
        self.centre_window(900, 600) # re-centre the window
        self.start_video_stream()  # restarts lives detection

    # method to capture a single frame from the webcam feed and display it
    def capture_frame(self):
        if self.cap and self.running:
            ret, frame = self.cap.read() # captures a single frame from the webcam livestream
            if ret:
                self.stop_video_stream() # stops live feed to freeze the frame
                imgtk = self.predict_frame(frame, False) # make prediction on frame
                self.image_label.imgtk = imgtk
                self.image_label.configure(image=imgtk) # displays image
                self.resize_display(imgtk.width(), imgtk.height())

    #method to resize the main window to accomodate for different image size
    def resize_display(self, width, height):
        self.left_frame.pack_propagate(False) # to prevent the frame from shrinking to fit the image
        self.left_frame.config(width=width, height=height)
        self.image_label.config(width=width, height=height)
        total_width = width + 300 # to add the width of the right section
        total_height = max(height, 600)
        self.centre_window(total_width, total_height) # re-centre the window after resizing

    # method to centre the main window
    def centre_window(self, width, height):
        self.root.update_idletasks()  # to check if layout calculations are up to date
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2) # for the horizontal centre
        y = (screen_height // 2) - (height // 2) # for the vertical centre
        self.root.geometry(f"{width}x{height}+{x}+{y}") #appliesnew size and position

    # returns image with prediction
    def predict_frame(self, frame, resize):
        img = self.detector.predict(frame) # make prediction on frame
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert image from BGR to RGB

        # checks if image should be resized
        if resize:
            img = Image.fromarray(img).resize((625, 625))
        else:
            img = Image.fromarray(img)

        # converts image to ImageTK object
        imgtk = ImageTk.PhotoImage(img)
        return imgtk

    # changes state of predict variable
    def start_prediction(self):
        self.predict = True
