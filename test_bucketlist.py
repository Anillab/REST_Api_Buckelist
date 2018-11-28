import unittest
import os
import json
from app import create_app,db

class Test_Case_Bucketlist(unittest.TestCase):

    def SetUp(self):
        self.app=create_app(config_name='testing')
        self.client=self.app.test_client
        self.bucketlist={'name':'Take a road trip to SouthAfrica'}

        # binds the app to the current context
        with self.app_context():
            db.create_all()

    def tearDown(self):
        '''
        tear down all initialized variables
        '''
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
        unittest.main()
