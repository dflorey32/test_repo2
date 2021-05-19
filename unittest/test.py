from unittest import TestCase
import sys
from mathlib.math import Math

class MathTest(TestCase):
    def testadd(self):
        m = Math()
        self.assertEqual(m.add(2,5), 7)

    def testsub(self):
        m = Math()
        self.assertEqual(m.sub(2,5),-3)



if __name__ == "__main__":
    unittest.main()
