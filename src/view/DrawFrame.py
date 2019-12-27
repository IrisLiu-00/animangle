from .FrameDisplay import FrameDisplay


class DrawFrame(FrameDisplay):
    """Displays a keyframe in a graphic manner, and allows the user to edit frames."""

    def __init__(self, animation, master):
        """Produces a DrawFrame based on the given model, set to displaying the first frame."""
        super().__init__(master)
        self._anim = animation
        self._curKey = 0

    def render(self):
        """Display the view."""
        self.displayFrame(self._anim.keyFrameAt(self._curKey))

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