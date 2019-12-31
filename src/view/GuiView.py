import tkinter as tk
from tkinter import filedialog, messagebox
from src.view.DrawFrame import DrawFrame
from src.view.PlayFrame import PlayFrame


class GuiView():
    """A graphical view for an animation, which is the main window the user interacts with."""

    def __init__(self, animation):
        """Produces a GuiView based on the given model.

        Args:
            animation (Animation): contains data for the animation to display todo read only?
        """
        self._features = None
        self._root = tk.Tk()
        self._playing = PlayFrame(animation, self._root)  # panel for playing the animation
        self._drawing = DrawFrame(animation, self._root)  # panel for drawing on stuff
        self._playing.grid(row=0, column=0, sticky="nsew")
        self._drawing.grid(row=0, column=0, sticky="nsew")
        self._drawing.tkraise()
        self._root.focus_set()
        self._root.title("Animangle")

        menubar = tk.Menu(self._root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self._openFile)
        filemenu.add_command(label="Save", command=self._saveFile)
        menubar.add_cascade(label="File", menu=filemenu)
        self._root.config(menu=menubar)

        # configuring the callbacks
        def startAnimation(_):
            self._playing.tkraise()
            self._playing.togglePlay(True)
            self._playing.render()

        def stopAnimation(_):
            self._playing.togglePlay(False)
            self._drawing.tkraise()
            self._drawing.render()

        def navForward(_):
            self._drawing.setToNext()
            self._drawing.render()

        def navBackward(_):
            self._drawing.setToPrev()
            self._drawing.render()

        self._root.bind("<Return>", startAnimation)
        self._root.bind("<space>", stopAnimation)
        self._root.bind("<Right>", navForward)
        self._root.bind("<Left>", navBackward)
        self.render()

    def makeVisible(self):
        """Make this view visible."""
        self._root.mainloop()

    def render(self):
        """Display the view."""
        self._drawing.render()

    def setToKey(self, keyIdx):
        """Make the given key visible, if possible."""
        self._drawing.setToKey(keyIdx)

    def addFeatures(self, features):
        """Add a callback to events raised by this view."""
        self._drawing.addFeatures(features)
        self._playing.addFeatures(features)
        self._root.bind("n", lambda evt: features.requestNewFrame())
        self._features = features

    def swapAnim(self, anim):
        self._playing.swapAnim(anim)
        self._drawing.swapAnim(anim)

    def displayMsg(self, msg: str):
        messagebox.showinfo(message=msg)

    def _openFile(self):
        """Displays a dialog to open a file, then calls the appropriate Features method to handle opening a file."""
        if self._features:
            filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("animangle files", "*.animangle"), ("all files", "*.*")))
            self._features.requestOpen(open(filename))

    def _saveFile(self):
        """Displays a dialog to save a file, then calls the appropriate Features method to handle saving a file."""
        if self._features:
            filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                    filetypes=(
                                                    ("animangle files", "*.animangle"), ("all files", "*.*")))
            self._features.requestSave(open(filename, "w"))
