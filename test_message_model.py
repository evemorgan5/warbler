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
        User.query.delete()

        u1 = User.signup("u1", "u1@email.com", "password", None)
        m1 = Message(text='Hello')
        u1.messages.append(m1)
        db.session.commit()

        self.u1_id = u1.id
        self.m1_id = m1.id


        self.client = app.test_client()

    def tearDown(self):
        db.session.rollback()

    def test_message_model(self):
        u1 = User.query.get(self.u1_id)

        self.assertEqual(len(u1.messages), 1)
        self.assertEqual(u1.messages[0].text, 'Hello')

