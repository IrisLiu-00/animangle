from model.AnimationBuilder import text2Anim, FileFormatException
from model.Posn import Posn
from view.TextualView import TextualView


class BasicController:
    """Manages user interactions for an animator."""

    def __init__(self, animator, view):
        """Creates a controller based on the given model and view."""
        self._anim = animator
        self._view = view

    def go(self):
        """Start the application."""
        self._view.addFeatures(self)
        self._view.makeVisible()

    def requestNewLine(self, keyIdx: int):
        """Respond to a request from the view to begin drawing a new line.

        Args:
            keyIdx (int): index of the key frame to draw the line on
        """
        self._anim.startNewLine(keyIdx)

    def requestAddPix(self, keyIdx: int, x: int, y: int):
        """Adds a pixel to the model at the given location.

        Args:
            keyIdx (int): index of the key frame to draw the pixel on
            x (int): x coordinate of the pixel
            y (int): y coordinate of the pixel
        """
        self._anim.addPix(keyIdx, Posn(x, y))
        self._view.render()

    def requestNewFrame(self):
        """Adds a new frame to the animation, and displays it."""
        self._anim.addFrame()
        self._view.setToKey(self._anim.numKeyFrames() - 1)
        self._view.render()

    def requestOpen(self, file):
        """Opens the given file, and displays the new animation on the view. If the file is improperly formatted,
        displays a message on the view.
        Args:
            file (file object): the file to open
        """
        with file:
            try:
                newAnim = text2Anim(file)
                self._view.swapAnim(newAnim)
                if newAnim.numKeyFrames() < 1:
                    newAnim.addFrame()
                self._view.setToKey(0)
                self._view.render()
            except FileFormatException as e:
                self._view.displayMsg(str(e))

    def requestSave(self, file):
        """Saves the current animation to the given file."""
        with file:
            view = TextualView(self._anim, file)
            view.render()
