import unittest

class TestMyFunction(unittest.TestCase):

    def test_my_function(self):
        arg = None
        self.assertIsNone( None)

if __name__ == '__main__':
    unittest.main()



t=TestMyFunction()
t.test_my_function()
"""
assertEqual(val,expected)
assertNotEqual(val,notexpected)
assertNone(val)
assertNotNone(val)
assertFalse(val)
assertTrue(val)
"""