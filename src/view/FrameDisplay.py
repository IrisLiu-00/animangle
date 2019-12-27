from tkinter import Frame, Canvas, ALL, TclError
from src.model.Frame import Frame as AniFrame

class FrameDisplay(Frame):
    """A class that can display frames in an animation"""

    def __init__(self, master):
        """Produces a FrameDisplay based on the given model."""
        super().__init__(master)
        #todo: make this resizable?
        self._width = 700
        self._height = 600
        self._canvas = Canvas(self, width=self._width, height=self._height)
        self._canvas.pack()

    def displayFrame(self, frame: AniFrame):
        """Displays the given frame.
        Args:
            frame (src.model.Frame): a frame from an animation to display
        """
        try:
            self._canvas.delete(ALL)
        except TclError: # catching if the window was closed
            return
        self._canvas.create_rectangle((0, 0, self._width, self._height), fill = "white") #fill bg
        # draw lines between pairs of pixels
        lines = frame.getLines()
        for line in lines:
            for i in range(len(line) - 1):
                thisPos = line[i]
                nextPos = line[i + 1]
                self._canvas.create_line(thisPos.x, thisPos.y, nextPos.x, nextPos.y, width = 3)
