from .Posn import Posn

class Frame:
    """A class representing a single frame in an animation. A frame may contain some number of lines,
    which are represented as a series of pixel locations."""

    def __init__(self):
        """Creates a Frame with no lines."""
        self._lines = []  # each line is a list of Posn

    def getLines(self):
        """Return all the lines in this frame. All lines are stored as an iterable, where each line is itself
        an iterable of Posns.
        """
        return list(tuple(line) for line in self._lines)  # defensive copying

    # todo functions below these count as pkg private
    def addLine(self):
        """Adds an empty line to this frame."""
        self._lines.append(list())

    def addPix(self, pix):
        """Adds a single pixel to the latest line in this frame.

        Args:
            pix (Posn): location of the pixel to be added
        """
        if not self._lines:
            raise ValueError("No lines in this frame yet")
        self._lines[len(self._lines) - 1].append(pix)

    def betweensTo(self, nextKey, numBetween):
        """Creates the given number of in betweens between this frame and the next key frame.

        Args:
            nextKey (Frame): the next key frame
            numBetween (int): number of in betweens to generate

        Returns:
            iterable of Frames
        """
        thisLines = list()
        nextLines = list()
        lineidx = 0
        # normalize both sets of lines to have the same num lines, each pair of lines w same len
        while (lineidx < len(self._lines)) or (lineidx < len(nextKey._lines)):
            if lineidx >= len(self._lines):  # no more lines in this frame
                self._copyLine(nextLines, thisLines, nextKey._lines[lineidx])
            elif lineidx >= len(nextKey._lines):  # no more lines in next frame
                self._copyLine(thisLines, nextLines, self._lines[lineidx])
            else:  # get the preexisting line for both and pad them
                self._copyBothLines(thisLines, nextLines, self._lines[lineidx], nextKey._lines[lineidx])
            lineidx += 1

        betweens = [Frame() for i in range(numBetween)]  # empty frames for all the betweens

        for i in range(len(thisLines)):
            thisLine = thisLines[i]
            nextLine = nextLines[i]
            for f in betweens:
                f.addLine()
            for j in range(len(thisLine)):
                thisPix = thisLine[j]
                nextPix = nextLine[j]
                xstep = (nextPix.x - thisPix.x) / numBetween
                ystep = (nextPix.y - thisPix.y) / numBetween
                lastx = thisPix.x
                lasty = thisPix.y
                for f in betweens:
                    lastx += xstep
                    lasty += ystep
                    f.addPix(Posn(int(lastx), int(lasty)))
        return betweens

    # lines of diff length get pixels padded to the end, so they have teh same num of pixels
    # diff num of lines > add all pix to midpoint of the extra line

    def _copyLine(self, copyTo, fabricateTo, line):
        """Copies given line to the copyTo list of lines, adds a line of same len to fabricateTo"""
        midPix = line[len(line) // 2]
        copyTo.append(line)  # copy the same line to this line set
        fabricateTo.append([midPix for pix in line])  # same length as the line

    def _copyBothLines(self, lista, listb, linea, lineb):
        """Copies lines to corresponding list of lines, adding pix at the end so both lines are same len"""
        diff = len(linea) - len(lineb)
        if diff > 0:
            lista.append(linea)
            self._addPadded(listb, lineb, diff)
        elif diff < 0:
            listb.append(lineb)
            self._addPadded(lista, linea, -diff)
        else:
            listb.append(lineb)
            lista.append(linea)

    def _addPadded(self, list, line, diff):
        """Adds the line to the list, lengthened by diff"""
        toAdd = [pix for pix in line]
        lastPix = line[len(line) - 1]  # assuming line is nonempty
        toAdd.extend([lastPix for i in range(diff)])
        list.append(toAdd)

    def __repr__(self):
        return f"Frame {self._lines!r}"
