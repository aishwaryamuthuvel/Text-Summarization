import unittest
from scorer import *

class ScorerTest(unittest.TestCase):

    def test_empty(self):
        content = 'This is my sentences.  With another'
        reference = 'With another.  This is my paragraph'

        s = Scorer()
        s.add(content, reference, 0.654)

        avg = s.averages()
        self.assertEqual(avg['cosine'], 0.654)
        self.assertEqual(avg['rouge-1']['f'], 0.8333333283333335)
        self.assertEqual(avg['rouge-1']['r'], 0.8333333333333334)
        self.assertEqual(avg['rouge-1']['p'], 0.8333333333333334)
        self.assertEqual(avg['rouge-2']['f'], 0.5999999950000001)
        self.assertEqual(avg['rouge-2']['r'], 0.6)
        self.assertEqual(avg['rouge-2']['p'], 0.6)
        self.assertEqual(avg['rouge-l']['f'], 0.8333333333328333)
        self.assertEqual(avg['rouge-l']['r'], 0.8333333333333334)
        self.assertEqual(avg['rouge-l']['p'], 0.8333333333333334)


if __name__ == '__main__':
    unittest.main()

