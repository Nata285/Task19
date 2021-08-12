
import yandex

import unittest



class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(yandex.add_folder('test'), 201)


    def tearDown(self):

        yandex.delete_folder('test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()