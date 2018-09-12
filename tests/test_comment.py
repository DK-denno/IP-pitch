import unittest
from .main import db
from app.models import Comments

class CommentmModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comments(id=1,user_name='a')
   
    def tearDown(self):
        Comment.query.delete()
        

    def test_instance(self):
        self.assertEqual(self.new_comment.comment,'a')
    
        
    def test_save_comment(self):
        self.new_comment.save_post()
        self.assertTrue(len(Comments.query.all())>0)
    
    def test_get_comment_by_id(self):

        self.new_comment.save_review()
        got_comment = Comments.get_comment(1)
        self.assertTrue(len(got_comment) == 1)



if __name__ == '__main__':
    unittest.main()
