import unittest
from app import db
from app.models import Post

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_post = Post(1,'a','b','c','d')
   
    def tearDown(self):
        Review.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertEqua(self.new_post.id,1)
        self.assertEqua(self.new_post.title,'a')
        self.assertEqua(self.new_post.post,'b')
        self.assertEqua(self.new_post.posted,'c')
        self.assertEqua(self.new_post.category,'d')
    
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)
    
    def test_get_post_by_id(self):

        self.new_post.save_post()
        got_post = Post.get_post(1)
        self.assertTrue(len(got_post) == 1)


if __name__ == '__main__':
    unittest.main()
