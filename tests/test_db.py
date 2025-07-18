import unittest
from peewee import *

from app import TimelinePost

<<<<<<< Updated upstream
# create an in-memory test or dummy database for testing
test_db = SqliteDatabase(':memory:')
MODELS = [TimelinePost]

class TestTimelinePost(unittest.TestCase):
    # run before each test
    def setUp(self):

        # bind models to test_db
         test_db.bind([TimelinePost], bind_refs=False, bind_backrefs=False)
         test_db.connect()
         test_db.create_tables(MODELS)

    # run after each test
=======
MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

>>>>>>> Stashed changes
    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

<<<<<<< Updated upstream
    # test for timeline posts
    def test_timeline_post(self):
        # create two timeline posts to test
        TimelinePost.create(name='John Doe', email='johndoe@gmail.com', content='Hello world, I\'m John')
        TimelinePost.create(name='Jane Doe', email='janedoe@gmail.com', content='Hello world, I\'m Jane')
        
        # get timeline posts
        first_post = TimelinePost.get_by_id(1)
        second_post = TimelinePost.get_by_id(2)
        
        # assert that the ids of the posts are equal to their respective ids, 1 and 2
        self.assertEqual(first_post.id, 1)
        self.assertEqual(second_post.id, 2)
        
        # assert that the names of the posts are equal to their respective names, John Doe and Jane Doe
        self.assertEqual(first_post.name, 'John Doe')
        self.assertEqual(second_post.name, 'Jane Doe')
        
        # assert that the emails of the posts are equal to their respective emails, johndoe@gmail.com and janedoe@gmail.com
        self.assertEqual(first_post.email, 'johndoe@gmail.com')
        self.assertEqual(second_post.email, 'janedoe@gmail.com')
        
        # assert that the content of the posts are equal to their respective contents
        self.assertEqual(first_post.content, 'Hello world, I\'m John')
        self.assertEqual(second_post.content, 'Hello world, I\'m Jane')
        
        
=======
    def test_create_timeline_post(self):
        first_post = TimelinePost.create(
            name="John Doe",
            email="jonnydoe@gmail.com",
            content="Hi Mom!"
        )
        assert first_post.id == 1   # Only really works if db is empty since id is autoincrementing
        second_post = TimelinePost.create(
            name="Jane Doe",
            email="jdoe@gmail.com",
            content="Hi Dad!"
        )
        assert second_post.id == 2 
>>>>>>> Stashed changes
