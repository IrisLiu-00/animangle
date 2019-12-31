import re

from .Animation import Animation

# WERE REALLY WRITING A PARSER HUH. BASARD
from .Posn import Posn


def file2Anim(filename: str) -> Animation:
    """Builds an Animation from a file.
    The file should be formatted as following: each frame should be on a new line. Each line within a frame
    is enclosed in brackets, and each line is separated by a space. Each Posn within a line is separated by
    spaces and formatted as an ordered pair (x, y).
    For example: [(13, 15) (13, 16) (14, 17)] [(89, 60) (90, 61) (89, 61) (88, 61)]

    Args:
        filename (str): name of the file, including the relative path

    Returns:
        Animation : the created animation

    Raises:
        FileNotFoundError: if the given file does not exist
        FileFormatException: if the file does not follow the correct format
    """
    with open(filename, "r") as file:
        return text2Anim(file)


def text2Anim(source):
    """Builds an Animation from a readable source of text, such as a file.
    The text should be formatted as following: each frame should be on a new line. Each line within a frame
    is enclosed in brackets, and each line is separated by a space. Each Posn within a line is separated by
    spaces and formatted as an ordered pair (x, y).
    For example: [(13, 15) (13, 16) (14, 17)] [(89, 60) (90, 61) (89, 61) (88, 61)]

    Args:
        source (file object): the source of text

    Returns:
        Animation : the created animation

    Raises:
        FileFormatException: if the file does not follow the correct format
    """
    anim = Animation()
    keyIdx = 0
    for frame in source:  # each textual line in the file is one animation frame
        if keyIdx != 0:
            anim.addFrame()  # anim is already made w frame 0, so only add frame for rest
        if not re.fullmatch(r"(\[[^]]+\] *)*\s*", frame):
            raise FileFormatException(f"line {keyIdx} in file is improperly formatted")
        for line in re.findall(r"\[([^]]+)\]", frame):  # gets all the stuff between [..]
            _addLine(line, anim, keyIdx)
        keyIdx += 1
    return anim


def _addLine(linestr, anim, keyIdx):
    """Adds the positions represented in the given string as a line to the animation.

    Args:
        linestr (str): a string of all the Posns in the line
        anim (Animation): the Animation to add the line to
        keyIdx: the key frame to add the line to
    """
    if not re.fullmatch(r"(\(\d+, \d+\) *)*\s*", linestr):
        raise FileFormatException("File improperly formatted; expected ordered pairs within brackets")
    anim.startNewLine(keyIdx)
    for pos in re.findall(r"\((\d+, \d+)\)", linestr):
        coordList = [int(num) for num in pos.split(", ")]
        anim.addPix(keyIdx, Posn(*coordList))


class FileFormatException(Exception):
    """Exception for files that are improperly formatted"""
    pass
