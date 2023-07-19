import unittest
import torch

class MyTestCase(unittest.TestCase):
    def test_something(self):
        rnn = torch.nn.LSTM(10, 20, 2)
        input = torch.randn(5, 3, 10)
        h0 = torch.randn(2, 3, 20)
        c0 = torch.randn(2, 3, 20)
        output, (hn, cn) = rnn(input, (h0, c0))
        print(output)


if __name__ == '__main__':
    unittest.main()
