import unittest

from model.Animation import Animation
from model.AnimationBuilder import file2Anim
from model.Posn import Posn
from view.TextualView import TextualView


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.anim1 = Animation()
        self.anim1.startNewLine(0)
        self.anim1.addPix(0, Posn(0, 0))
        self.anim1.addPix(0, Posn(0, 1))
        self.anim1.addPix(0, Posn(0, 2))
        self.anim1.startNewLine(0)
        self.anim1.addPix(0, Posn(2, 0))
        self.anim1.addPix(0, Posn(3, 0))
        self.anim1.addPix(0, Posn(3, 1))
        self.anim1.addFrame()
        self.anim1.startNewLine(1)
        self.anim1.addPix(1, Posn(0, 0))
        self.anim1.addPix(1, Posn(1, 1))
        self.anim1.addPix(1, Posn(2, 2))
        self.anim1.addPix(1, Posn(3, 3))
        self.anim1.addFrame()
        self.anim1.startNewLine(2)
        self.anim1.addPix(2, Posn(0, 0))
        self.anim1.addPix(2, Posn(0, 1))
        self.anim1.addPix(2, Posn(0, 2))
        self.anim1.startNewLine(2)
        self.anim1.addPix(2, Posn(2, 0))
        self.anim1.addPix(2, Posn(2, 1))
        self.anim1.addPix(2, Posn(2, 2))
        self.anim1.addFrame()

    def test_text_view(self):
        with open(r"C:\Users\IrisL\Documents\PycharmProjects\Animator\src\resources\anim2.aml", "w") as file:
            view = TextualView(self.anim1, file)
            view.render()
        anim2 = file2Anim(r"C:\Users\IrisL\Documents\PycharmProjects\Animator\src\resources\anim2.aml")
        for i in range(self.anim1.numFrames()):
            self.assertEqual(anim2.frameAt(i), self.anim1.frameAt(i))
        self.assertEqual(self.anim1.numFrames(), anim2.numFrames())

if __name__ == '__main__':
    unittest.main()
