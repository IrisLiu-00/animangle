from .Frame import Frame
from .Posn import Posn

class Animation:
    """A class containing information about an animation, including key frames and in betweens."""

    numBetweens = 10

    def __init__(self):
        """Creates an Animation with a single starting key frame."""
        self._frames = [Frame()]  # private
        self._betweens = dict()  # dictionary from int (key frame idx) to list of frames following that key frame
        # the lists in this dict are always complete; if there is a list for a keyIdx, that list has all frames

    def numFrames(self) -> int:
        """Return the total number of frames in this animation, including in betweens."""
        return (len(self._frames) - 1) * (self.numBetweens + 1) + 1

    def numKeyFrames(self) -> int:
        """Return only the number of key frames in this animation."""
        return len(self._frames)

    def frameAt(self, idx: int):
        """Returns the frame at the given position, 0 indexed.

        Args:
            idx (int): position of the frame, 0 indexed

        Returns:
            Frame: the frame at the given index

        Raises:
            IndexError: if no frame exists at that location
        """
        prevKey = idx // (self.numBetweens + 1)  # previous or current key frame
        self._validateKeyIdx(prevKey)
        if (idx / (self.numBetweens + 1)) > len(self._frames):  # idx is for a between after last key
            raise IndexError("Frame index out of bounds")
        betweenIdx = idx % (self.numBetweens + 1)
        if betweenIdx == 0:
            return self.keyFrameAt(prevKey)
        if not prevKey in self._betweens:
            self._betweens[prevKey] = self._frames[prevKey].betweensTo(self._frames[prevKey + 1], self.numBetweens)
        return self._betweens[prevKey][betweenIdx - 1]

    # todo: read only frame? how to properly encapsulate frames

    def keyFrameAt(self, keyIdx: int):
        """Returns the key frame with the given index.

        Args:
            keyIdx (int): 0 indexed, counting only the key frames.

        Returns:
            Frame: the frame at the given index.

        Raises:
            IndexError: if no frame exists at that location
         """
        self._validateKeyIdx(keyIdx)
        return self._frames[keyIdx]

    def addFrame(self):
        """Adds a new keyframe to the end of this animation."""
        self._frames.append(Frame())

    def startNewLine(self, keyIdx: int):
        """Initializes a new line on the key frame at the given location, so that any pixels added are added to this new line.

        Args:
            keyIdx (int): 0 indexed, counting only the key frames.

        Raises:
            IndexError: if no frame exists at that location
         """
        self._validateKeyIdx(keyIdx)
        self._frames[keyIdx].addLine()
        self._clearCacheAround(keyIdx)

    def addPix(self, keyIdx: int, pix: Posn):
        """Adds a pixel to the last line that was added to the given key frame.

        Args:
            keyIdx (int): 0 indexed, counting only the key frames
            pix (Posn): location of the pixel to add

        Raises:
            IndexError: if no frame exists at that location
        """
        self._validateKeyIdx(keyIdx)
        self._frames[keyIdx].addPix(pix)
        self._clearCacheAround(keyIdx)

    def _validateKeyIdx(self, keyIdx: int):
        """Checks that the given index is for an existing key frame."""
        if (keyIdx >= len(self._frames) or keyIdx < 0):
            raise IndexError("No keyframe at index " + str(keyIdx))

    def _clearCacheAround(self, keyIdx: int):
        """Clears the betweens before and after this key idx, if they exist"""
        if (keyIdx != 0):
            self._betweens.pop(keyIdx - 1, None) #clear before
        self._betweens.pop(keyIdx, None) #clear after