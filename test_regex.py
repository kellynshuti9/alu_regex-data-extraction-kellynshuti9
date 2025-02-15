import unittest
from regex_extractor import RegexExtractor

class TestRegexExtractor(unittest.TestCase):
    def setUp(self):
        """Sets up a test string for validation."""
        self.text = """
        Contact us at support@example.com or info@test.org.
        Visit https://www.example.com and http://test.com/page.
        Call us at (123) 456-7890 or 123-456-7890.
        Your credit card 1234-5678-9012-3456 is valid.
        """
        self.extractor = RegexExtractor(self.text)

    def test_extract_emails(self):
        expected = ['support@example.com', 'info@test.org']
        self.assertEqual(self.extractor.extract_emails(), expected)

    def test_extract_urls(self):
        expected = ['https://www.example.com', 'http://test.com/page']
        self.assertEqual(self.extractor.extract_urls(), expected)

    def test_extract_phone_numbers(self):
        expected = ['(123) 456-7890', '123-456-7890']
        self.assertEqual(self.extractor.extract_phone_numbers(), expected)

    def test_extract_credit_card_numbers(self):
        expected = ['1234-5678-9012-3456']
        self.assertEqual(self.extractor.extract_credit_card_numbers(), expected)

if __name__ == '__main__':
    unittest.main()
