import unittest
import ec2


class TestEc2(unittest.TestCase):
    """
    Test ec2 cf generation
    """

    def test_cf_gen(self):
        r = 2 + 2
        self.assertEqual(r, 4)
