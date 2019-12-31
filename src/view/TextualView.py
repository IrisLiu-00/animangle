
class TextualView():
    """Textual represents an animation, where each key frame is represented as a single line in the text output. This
    view is compatible with the file reader in the AnimationBuilder module."""

    def __init__(self, anim, target):
        """Produces a textual view based on the given Animation, and writes to the given target.

        Args:
            anim (Animation): the model to base the view off of
            target (writable?): where to output the textual view
        """
        self.anim = anim
        self.target = target

    def makeVisible(self):
        """Make this view visible, which it already is."""
        pass

    def render(self):
        """Display the view as text outputted to the target"""
        toWrite = []
        for i in range(self.anim.numKeyFrames()):
            frame = self.anim.keyFrameAt(i)
            linelist = frame.getLines()
            for line in linelist:
                toWrite.append("[")
                for pos in line:
                    toWrite.append(f"({pos.x}, {pos.y}) ")
                toWrite.append("] ")
            if i != self.anim.numKeyFrames() - 1:
                toWrite.append("\n")
        self.target.write("".join(toWrite))


    def setToKey(self, keyIdx):
        """Make the given key visible. Does nothing because all keys are visible by default"""
        pass

    def addFeatures(self, features):
        """Add a callback to events raised by this view. Does nothing because this view raises no events."""
        pass
