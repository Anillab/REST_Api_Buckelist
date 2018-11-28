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

    def test_bucketlist_creation(self):
        '''
        Test API can create a bucketlist(POST request)
        '''
        response=self.client().post('/bucketlists',data=self.bucketlist)
        self.assertEqual(response.status_code,201)
        self.assertIn('Take a road trip to SouthAfrica',str(response.data))

    def test_api_get_all_bucketlists(self):
        '''
        Test API can get a bucketlist(GET request)
        '''
        response=self.client().post('/bucketlists',data=self.bucketlist)
        self.assertEqual(response.status_code,201)
        response=self.client().get('/bucketlists/')
        self.assertEqual(response.status_code,200)
        self.assertIn('Take a road trip to SouthAfrica',str(response.data))

    def test_api_get_bucketlist_by_id(self):
        response=self.client().post('/bucketlists',data=self.bucketlist)
        self.assertEqual(response.status_code,201)
        result_in_json=json.loads(response.data.decode('utf-8').replace("'","\""))
        result=self.client().get(
        '/bucketlists/{}'.format(result_in_json['id'])
        )
        self.assertEqual(result.status_code,200)
        self.assertIn('Take a road trip to SouthAfrica',str(response.data))
    def test_bucketlist_deletion(self):
        '''
        Test API can delete an existing bucketlist (delete request).
        '''
        response=self.client().post('/bucketlists',data={'name':'Eat,pray and love'})
        self.assertEqual(response.status_code,201)
        res=self.client().delete('/bucketlist/1')
        self.assertEqual(res.status_code,200)
        result=self.client().get('/bucketlist/1')
        self.assertEqual(result.status_code,404)

    def tearDown(self):
        '''
        tear down all initialized variables
        '''
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
        unittest.main()
