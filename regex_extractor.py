import re

class RegexExtractor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
        """Extracts all valid email addresses from the text."""
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, self.text)

    def extract_urls(self):
        """Extracts all valid URLs from the text."""
        pattern = r'https?://[^\s,]+(?<!\.)'  # Fixes trailing period issue
        return re.findall(pattern, self.text)

    def extract_phone_numbers(self):
        """Extracts phone numbers in common formats."""
        pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        return re.findall(pattern, self.text)

    def extract_credit_card_numbers(self):
        """Extracts credit card numbers in 16-digit formats."""
        pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        return re.findall(pattern, self.text)
