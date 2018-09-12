import unittest
from app import db
from app.models import Posts,User

class PostModelTest(unittest.TestCase):


    def tearDown(self):
        Posts.query.delete()
        
    def setUp(self):
        self.new_post = Posts(id=100,title='a',post='b',category='d')
   
       

    def test_instance(self):
        self.assertEqual(self.new_post.id,100)
        self.assertEqual(self.new_post.title,'a')
        self.assertEqual(self.new_post.post,'b')
        self.assertEqual(self.new_post.category,'d')
    
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Posts.query.all())>0)
    
    def test_get_post_by_id(self):

        self.new_post.save_post()
        got_post = Posts.get_post(1)
        self.assertTrue(len(got_post) > 0)


if __name__ == '__main__':
    unittest.main()
