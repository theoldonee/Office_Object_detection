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
        self.window_width = 1000
        self.window_height = 700
        self.root.geometry(f"{self.window_width}x{self.window_height}+400+150") # set size and location
        self.detector = Detector()
        self.predict = False


        # setting up the layout
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # left section: for image/webcam display
        self.left_frame = tk.Frame(main_frame, width=625, height=700, borderwidth=2, relief="solid")
        self.left_frame.pack(side="left", anchor="n", fill="y")
        self.left_frame.pack_propagate(False) # prevent frame from shrinking to fit contents
        self.image_label = tk.Label(self.left_frame)
        self.image_label.pack()

        # right section: button panel
        right_frame = tk.Frame(main_frame, width=375)
        right_frame.pack(fill="both")

        #header label
        header = Label(right_frame, text="Office Object Detection", fg="black", font=("Helvetica", 15))
        header.pack(pady=5)

        # upload image button
        upload_img_btn = GUIButton(right_frame, text="Upload Image", command=self.upload_image, font=("Helvetica", 12))
        upload_img_btn.pack(pady=10)
        upload_img_btn.config_colours(activeBG="green4", activeFG="white", bgcolour="SpringGreen3",
                                      fgcolour="white", hoverBG="green3", hoverFG="white")
        upload_img_btn.set_dimensions(height=1, width=16)

        #capture frame button
        capture_btn = GUIButton(right_frame, text="Capture", command=self.capture_frame, font=("Helvetica", 12))
        capture_btn.pack(pady=10)
        capture_btn.config_colours(activeBG="dodgerblue4", activeFG="white",  bgcolour="dodgerblue3", fgcolour="white", hoverBG="dodgerblue2", hoverFG="white")
        capture_btn.set_dimensions(height=1, width=16)

        #start live detection button
        self.live_stream_btn = GUIButton(right_frame, text="Start Live Detection", command=self.start_prediction, font=("Helvetica", 12))
        self.live_stream_btn.pack(pady=10)
        self.live_stream_btn.config_colours(activeBG="green4", activeFG="white",
                                       bgcolour="SpringGreen3", fgcolour="white", hoverBG="green3", hoverFG="white")

        # back button (returns to default livestream)
        back_btn = GUIButton(right_frame, text="Back",command=self.go_back,font =("Helvetica", 12))
        back_btn.pack(pady=10)
        back_btn.config_colours(activeBG="gray30", activeFG="white", bgcolour="gray60",
                                fgcolour="white",hoverBG="gray40", hoverFG="white")
        back_btn.set_dimensions(height=1, width=16)

        #quit button (ends program)
        quit_btn = GUIButton(right_frame, text="Quit",command=self.quit_app,  font=("Helvetica", 12))
        quit_btn.pack(pady=10)
        quit_btn.config_colours(activeBG="firebrick4", activeFG="white", bgcolour="firebrick3",
                                fgcolour="white", hoverBG="red", hoverFG="white")

        quit_btn.set_dimensions(height=1, width=16)

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
        frame = Image.open(path) # loads image from file
        imgtk = self.predict_frame(frame) # make prediction on frame
        self.image_label.imgtk = imgtk  # this prevents garbage collection
        self.image_label.configure(image=imgtk) # displays image in label

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
                    imgtk = self.predict_frame(frame)
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
        self.start_video_stream()  # restarts lives detection

    # method to capture a single frame from the webcam feed and display it
    def capture_frame(self):
        if self.cap and self.running:
            ret, frame = self.cap.read() # captures a single frame from the webcam livestream
            if ret:
                self.stop_video_stream() # stops live feed to freeze the frame
                imgtk = self.predict_frame(frame) # make prediction on frame
                self.image_label.imgtk = imgtk
                self.image_label.configure(image=imgtk) # displays image

    # returns image with prediction
    def predict_frame(self, frame):
        img = self.detector.predict(frame) # make prediction on frame
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert image from BGR to RGB
        img = Image.fromarray(img).resize((625, 625)) # resize image to window size
      
        # converts image to ImageTK object
        imgtk = ImageTk.PhotoImage(img)
        return imgtk

    # changes state of predict variable
    def start_prediction(self):
        # check if predict is true and video frames are being captured
        if self.predict and self.running:
            self.reset_live_btn()
        elif self.predict == False and self.running :
            self.predict = True
            self.live_stream_btn.config_colours(activeBG="firebrick4", activeFG="white", bgcolour="firebrick3",
                                fgcolour="white", hoverBG="red", hoverFG="white")
            self.live_stream_btn.config_text("Stop Live Detection")

    # reset live button
    def reset_live_btn(self):
        self.predict = False
        self.live_stream_btn.config_colours(activeBG="green4", activeFG="white",
                                    bgcolour="SpringGreen3", fgcolour="white", hoverBG="green3", hoverFG="white")
        self.live_stream_btn.config_text("Start Live Detection")