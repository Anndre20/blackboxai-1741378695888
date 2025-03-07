# Unit Tests for Automated Email Response Module

import unittest
from email_response import generate_response

class TestEmailResponse(unittest.TestCase):
    def test_generate_response(self):
        email_content = "Inquiry about order status."
        response = generate_response(email_content)
        self.assertIn("Thank you for your inquiry", response)  # Check if response contains expected text

if __name__ == '__main__':
    unittest.main()
