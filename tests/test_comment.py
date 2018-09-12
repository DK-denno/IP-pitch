import unittest
from app import db
from app.models import Posts,User,Comments

class CommentmModelTest(unittest.TestCase):

    def tearDown(self):
        Posts.query.delete()
        User.query.delete()
        Comments.query.delete()

    def setUp(self):
        self.new_comment = Comments(id=10,comment='a')
   
            

    def test_instance(self):
        self.assertEqual(self.new_comment.comment,'a')
    
        
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)
    
    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comment = Comments.get_comment(1)
        self.assertTrue(len(got_comment) == 0)



if __name__ == '__main__':
    unittest.main()
