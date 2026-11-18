import unittest
import requests
import os

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = os.getenv("OLLAMA_MODEL", "gemma4:e2b")

class TestOllamaEndpoint(unittest.TestCase):

    def test_server_responds(self):
        """Verify the server is running and lists models."""
        response = requests.get(f"{OLLAMA_URL}/api/tags")
        self.assertEqual(response.status_code, 200)
        self.assertIn("models", response.json())

    def test_generation(self):
        """Verify the model can generate a response."""
        payload = {
            "model":MODEL_NAME,
            "prompt": "Hello",
            "stream": False
        }
        response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json())

if __name__ == "__main__":
    unittest.main()

