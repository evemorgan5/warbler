"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_message_model.py


import os
from tokenize import String
from unittest import TestCase

from models import db, User, Message, Follows


# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class MessageModelTestCase(TestCase):

    def setUp(self):
        Message.query.delete()

        m1 = Message('Hello')
        m2 = Message('Goodbye')

        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        db.session.rollback()

    def test_message_model(self):
        m1 = Message.query.get(self.id)
        m2 = Message.query.get(self.id)

        self.assertEqual(m1.text, 'Hello') 
        self.assertEqual(m2.text, 'Goodbye')

    