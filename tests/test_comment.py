import unittest
from app import db
from app.models import Comment

class CommentmModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Post('a')
   
    def tearDown(self):
        Review.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertEqua(self.new_post.comment,'a')
    
        
    def test_save_comment(self):
        self.new_comment.save_post()
        self.assertTrue(len(Comment.query.all())>0)
    
    def test_get_comment_by_id(self):

        self.new_comment.save_review()
        got_comment = Comment.get_comment(1)
        self.assertTrue(len(got_comment) == 1)



if __name__ == '__main__':
    unittest.main()
