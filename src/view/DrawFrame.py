from .FrameDisplay import FrameDisplay
from tkinter import ALL


class DrawFrame(FrameDisplay):
    """Displays a keyframe in a graphic manner, and allows the user to edit frames."""

    def __init__(self, animation, master):
        """Produces a DrawFrame based on the given model, set to displaying the first frame."""
        super().__init__(animation, master)
        self._curKey = 0

    def render(self):
        """Display the view, by showing the current keyframe and an onion skin for the previous frame."""
        if self._curKey == 0:
            self._displayFrame(self._anim.keyFrameAt(self._curKey))
        else:
            self._canvas.delete(ALL)
            self._canvas.create_rectangle((0, 0, self._width, self._height), fill="white")  # fill bg
            self._displayFrameTransparent(self._anim.keyFrameAt(self._curKey - 1), "#838c9c") #onion skin gray
            self._displayFrameTransparent(self._anim.keyFrameAt(self._curKey), "black")
            #todo: theres a mouse lag when we try to draw lots of lines - need to somehow cache drawing

    def setToKey(self, keyIdx):
        self._curKey = keyIdx

    def setToNext(self):
        self._curKey = min(self._curKey + 1, self._anim.numKeyFrames() - 1)

    def setToPrev(self):
        self._curKey = max(self._curKey - 1, 0)

    def addFeatures(self, features):
        """Add a callback to events raised by this view."""
        def callNewLine(event):
            features.requestNewLine(self._curKey)
            features.requestAddPix(self._curKey, event.x, event.y)
        self._canvas.bind("<Button-1>", callNewLine)
        self._canvas.bind("<B1-Motion>", lambda evt : features.requestAddPix(self._curKey, evt.x, evt.y))