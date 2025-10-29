from tkinter import Button

class GUIButton:
    def __init__(self, root, **kwargs):
        # get window
        self.root = root

        # use keyword arguments to set parameters
        self.text = kwargs.get("text", "Untitled")
        self.command = kwargs.get("command", self.void_function)
        self.font = kwargs.get("font", ("Helvetica", 15))
        self.bg = kwargs.get("bgcolour", "white")
        self.fg = kwargs.get("fgcolour", "black")
        self.active_bg = kwargs.get("activeBG", "white")
        self.active_fg = kwargs.get("activeFG", "black")
        self.hover_bg = kwargs.get("hoverBG", "white")
        self.hover_fg = kwargs.get("hoverFG", "black")
        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)


        # create button
        self.button = Button(
            self.root, text=self.text, command=self.command, font=("Helvetica", 15), 
            borderwidth=0, highlightthickness=0, bg=self.bg, fg=self.fg, activebackground=self.active_bg, activeforeground=self.active_fg
        )

        # bind events to button
        self.button.bind("<Enter>", self.on_hover)
        self.button.bind("<Leave>", self.on_leave)
        
        # place button on screen
        self.button.place(x=self.x, y=self.y)

    # tracks hover events
    def on_hover(self, event):
        self.button.config(bg=self.hover_bg, fg=self.hover_fg)
    
    # tracks leave events
    def on_leave(self, event):
        self.button.config(bg=self.bg, fg=self.fg)

    # configures button colours
    def config_colours(self, **kwargs):
        self.bg = kwargs.get("bgcolour", self.bg)
        self.fg = kwargs.get("fgcolour", self.fg)
        self.active_bg = kwargs.get("activeBG", self.active_bg)
        self.active_fg = kwargs.get("activeFG", self.active_fg)
        self.hover_bg = kwargs.get("hoverBG", self.hover_bg)
        self.hover_fg = kwargs.get("hoverFG", self.hover_fg)

        self.button.config(bg=self.bg, fg=self.fg, activebackground=self.active_bg, activeforeground=self.active_fg)

    # configures button dimentions
    def set_dimensions(self, **kwargs):

        self.height = kwargs.get("height", 5)
        self.width = kwargs.get("width", 5)

        self.button.config(height= self.height, width= self.width)

    # configure button text
    def config_text(self, text):
        self.text = text
        self.button.config(text=self.text)

    # void function
    def void_function(self):
        pass

    #alows the custom GUIButton to be packed into the layout
    def pack(self, **kwargs):
        self.button.pack(**kwargs)
