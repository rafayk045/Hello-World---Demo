import unittest
import sys
from io import StringIO
from hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello World")

if __name__ == '__main__':
    unittest.main()