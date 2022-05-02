
import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.new_article=Article({'id':'citizn','name':'citizen'},'bluesky break ceiling','Ogaye-Michael','blueskies beat the horizons in final touch to reach the finals','https:\\maurictin.sports.img.koyt','2022-05-02','the blue stars demolished the eageles in the first round','www.tuzo.co.ke')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_length(self):
        self.assertEqual(len(self.new_article),8)
    
if __name__=='__main__':
        unittest.run()    