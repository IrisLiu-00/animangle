import unittest
from src.model.Animation import Animation
from src.model.Posn import Posn


class TestAnimation(unittest.TestCase):
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

    def test_num_frames(self):
        self.assertEqual(23, self.anim1.numFrames())
        self.anim1.addFrame()
        self.assertEqual(34, self.anim1.numFrames())

    def test_num_keys(self):
        self.assertEqual(3, self.anim1.numKeyFrames())
        self.anim1.addFrame()
        self.assertEqual(4, self.anim1.numKeyFrames())

    def test_key_frame_at(self):
        actual = self.anim1.keyFrameAt(0).getLines()
        expect = [(Posn(0, 0), Posn(0, 1), Posn(0, 2)), (Posn(2, 0), Posn(3, 0), Posn(3, 1))]
        self.assertEqual(expect, actual)
        actual = self.anim1.keyFrameAt(1).getLines()
        expect = [(Posn(0, 0), Posn(1, 1), Posn(2, 2), Posn(3, 3))]
        self.assertEqual(expect, actual)
        actual = self.anim1.keyFrameAt(2).getLines()
        expect = [(Posn(0, 0), Posn(0, 1), Posn(0, 2)), (Posn(2, 0), Posn(2, 1), Posn(2, 2))]
        self.assertEqual(expect, actual)

    def test_frame_at_key(self):
        self.assertEqual(self.anim1.keyFrameAt(0), self.anim1.frameAt(0))
        self.assertEqual(self.anim1.keyFrameAt(1), self.anim1.frameAt(11))
        self.assertEqual(self.anim1.keyFrameAt(2), self.anim1.frameAt(22))

    def test_frame_at_between1(self):
        frame = self.anim1.frameAt(1)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(0, 2), Posn(0, 2)), (Posn(2, 0), Posn(3, 0), Posn(3, 0))]
        self.assertEqual(frameLines, frame.getLines())
        frame = self.anim1.frameAt(5)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(1, 2), Posn(1, 2)), (Posn(2, 0), Posn(3, 0), Posn(3, 0))]
        self.assertEqual(frameLines, frame.getLines())
        frame = self.anim1.frameAt(10)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(1, 2), Posn(2, 3)), (Posn(3, 0), Posn(3, 0), Posn(3, 0))]
        self.assertEqual(frameLines, frame.getLines())

    def test_frame_at_between2(self):
        frame = self.anim1.frameAt(12)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(1, 2), Posn(2, 2)), (Posn(2, 0), Posn(2, 1), Posn(2, 1))]
        self.assertEqual(frameLines, frame.getLines())
        frame = self.anim1.frameAt(20)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(0, 2), Posn(0, 2)), (Posn(2, 0), Posn(2, 1), Posn(2, 1))]
        self.assertEqual(frameLines, frame.getLines())

    def test_frame_at_post_add_line(self):
        frame = self.anim1.frameAt(12)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(1, 2), Posn(2, 2)), (Posn(2, 0), Posn(2, 1), Posn(2, 1))]
        self.assertEqual(frameLines, frame.getLines())
        frame = self.anim1.frameAt(16)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(1, 2), Posn(1, 2)), (Posn(2, 0), Posn(2, 1), Posn(2, 1))]
        self.assertEqual(frameLines, frame.getLines())
        self.anim1.startNewLine(1)
        self.anim1.addPix(1, Posn(0, 0))
        self.anim1.addPix(1, Posn(0, 1))
        self.anim1.addPix(1, Posn(0, 2))
        frame = self.anim1.frameAt(12)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(1, 2), Posn(2, 2)), (Posn(0, 0), Posn(0, 1), Posn(0, 2))]
        self.assertEqual(frameLines, frame.getLines())
        frame = self.anim1.frameAt(16)
        frameLines = [(Posn(0, 0), Posn(0, 1), Posn(1, 2), Posn(1, 2)), (Posn(1, 0), Posn(1, 1), Posn(1, 2))]
        self.assertEqual(frameLines, frame.getLines())

    def test_frame_at_bad_idx(self):
        self.assertRaises(IndexError, Animation.frameAt, self.anim1, -3)
        self.assertRaises(IndexError, Animation.frameAt, self.anim1, 33)
        self.assertRaises(IndexError, Animation.keyFrameAt, self.anim1, -3)
        self.assertRaises(IndexError, Animation.keyFrameAt, self.anim1, 3)

    def test_edit_frame_at_bad_idx(self):
        self.assertRaises(IndexError, Animation.startNewLine, self.anim1, -3)
        self.assertRaises(IndexError, Animation.startNewLine, self.anim1, 33)
        self.assertRaises(IndexError, Animation.addPix, self.anim1, -3, Posn(0, 0))
        self.assertRaises(IndexError, Animation.addPix, self.anim1, 3, Posn(0, 0))


if __name__ == '__main__':
    unittest.main()
