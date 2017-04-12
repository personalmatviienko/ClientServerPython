import unittest
import Client
import Server


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        Server.start(8080)

    def tearDown(self):
        Server.stop()

    def test_post_positive(self):
        response = Client.postRequest("test message", "3")
        self.assertTrue(response.text == 'test message' and response.status_code == 200)

    def test_post_negative_plus(self):
        response = Client.postRequest("test message", "10001")
        self.assertTrue(response.text == 'Queue is out of index, it should be from 0 to 10000'
                        and response.status_code == 200)

    def test_post_negative_minus(self):
        response = Client.postRequest("test message", "-1")
        self.assertTrue(response.text == 'Queue is out of index, it should be from 0 to 10000'
                        and response.status_code == 200)

    def test_get_negative_plus(self):
        response = Client.getRequest("10001")
        self.assertTrue(response.text == 'Queue is out of index, it should be from 0 to 10000'
                        and response.status_code == 200)

    def test_get_negative_minus(self):
        response = Client.getRequest("-1")
        self.assertTrue(response.text == 'Queue is out of index, it should be from 0 to 10000'
                        and response.status_code == 200)

    def test_get_empty_queue(self):
        response = Client.getRequest("1")
        self.assertTrue(response.text == 'Queue is empty'
                        and response.status_code == 200)

    def test_get_positive(self):
        Client.postRequest("test message", "0")
        response = Client.getRequest("0")
        self.assertTrue(response.text == 'test message'
                        and response.status_code == 200)

    def test_get_delete_message(self):
        Client.postRequest("test message", "0")
        Client.getRequest("0")
        response = Client.getRequest("0")
        self.assertTrue(response.text == 'Queue is empty'
                        and response.status_code == 200)
