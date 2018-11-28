
    def tearDown(self):
        '''
        tear down all initialized variables
        '''
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
        unittest.main()
