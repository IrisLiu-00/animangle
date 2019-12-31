import unittest
from src.model.AnimationBuilder import file2Anim, FileFormatException
from src.model.Posn import Posn


class TestBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self.anim1 = file2Anim(r"C:\Users\IrisL\Documents\PycharmProjects\Animator\src\resources\anim1.aml")

    def test_frames(self):
        exp = [(Posn(1, 2), Posn(3, 4), Posn(5, 6))]
        actual = self.anim1.keyFrameAt(0).getLines()
        self.assertEqual(exp, actual)
        exp = []
        self.assertEqual(exp, self.anim1.keyFrameAt(1).getLines())
        exp = [(Posn(3, 4),), (Posn(17, 8), Posn(9, 10), Posn(11, 12), Posn(9, 4))]
        self.assertEqual(exp, self.anim1.keyFrameAt(2).getLines())
        exp = [(Posn(5, 7), Posn(6, 4)), (Posn(13, 80) , Posn(4, 5)), (Posn(1, 2),)]
        self.assertEqual(exp, self.anim1.keyFrameAt(3).getLines())

    def test_mt(self):
        anim2 = file2Anim(r"C:\Users\IrisL\Documents\PycharmProjects\Animator\src\model\__init__.py")
        self.assertEqual(1, anim2.numFrames())

    def test_error1(self):
        self.assertRaises(FileFormatException, file2Anim, "formaterror1.aml")
        self.assertRaises(FileFormatException, file2Anim, "formaterror2.aml")
        self.assertRaises(FileFormatException, file2Anim, "formaterror3.aml")

    # test an empty file (empty anim)
    # test a nonexistent file (riase error)

if __name__ == '__main__':
    unittest.main()