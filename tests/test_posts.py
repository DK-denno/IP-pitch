import unittest
from app import db
from app.models import Posts

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_post = Posts(1,'a','b','c','d')
   
    def tearDown(self):
        Post.query.delete()
       

    def test_instance(self):
        self.assertEqua(self.new_post.id,1)
        self.assertEqua(self.new_post.title,'a')
        self.assertEqua(self.new_post.post,'b')
        self.assertEqua(self.new_post.posted,'c')
        self.assertEqua(self.new_post.category,'d')
    
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Posts.query.all())>0)
    
    def test_get_post_by_id(self):

        self.new_post.save_post()
        got_post = Posts.get_post(1)
        self.assertTrue(len(got_post) == 1)


if __name__ == '__main__':
    unittest.main()
