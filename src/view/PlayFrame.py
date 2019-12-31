from .FrameDisplay import FrameDisplay

class PlayFrame(FrameDisplay):
    """Displays all the frames in an animation in sequence."""

    _gap = 1/24 #pause between frames

    def __init__(self, animation, master):
        """Produces a PlayFrame based on the given model."""
        super().__init__(animation, master)
        self._playing = False

    def render(self):
        """Play the animation by displaying all the frames in sequence."""
        curFrame = 0
        def renderHelp():
            nonlocal curFrame
            if self._playing:
                self._displayFrame(self._anim.frameAt(curFrame))
                curFrame = (curFrame + 1) % self._anim.numFrames()
                self.master.after(40, renderHelp)
        renderHelp()

    def togglePlay(self, playing):
        self._playing = playing

    def addFeatures(self, features):
        """Does nothing; this object raises no events."""