import unittest
from fastapi.testclient import TestClient
from main import app

class TestWebSocketEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_websocket_connection(self):
        with self.client.websocket_connect("/ws") as websocket:
            response = websocket.receive_text()
            self.assertEqual(response, "Connected")

    def test_websocket_message(self):
        with self.client.websocket_connect("/ws") as websocket:
            message = "Hello, world!"
            websocket.send_text(message)
            response = websocket.receive_text()
            self.assertEqual(response, message)

if __name__ == "__main__":
    unittest.main()