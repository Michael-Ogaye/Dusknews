import unittest
from app.models import Source

class Sourcetest(unittest.TestCase):
    """
    Testing of the source class

    """
    def setUp(self):
        """
        runs before every tests
        """
        self.new_source=Source('Abc','putvnews','this is a sports analysis channel','en','ken','sports','www.brewsports.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_length(self):
        self.assertEqual(len(self.new_source),7)

if __name__=='__main__':
        unittest.run()