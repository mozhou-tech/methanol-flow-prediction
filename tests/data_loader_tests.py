import unittest

from src.data_loader import read_flow_speed


class MyTestCase(unittest.TestCase):
    def test_read_flow_speed(self):
        data = read_flow_speed()
        print(data)


if __name__ == '__main__':
    unittest.main()
