# tests/test_quote_api_adapter.py

import unittest
from integration.quote_api_adapter import QuoteApiAdapter

class TestQuoteApiAdapter(unittest.TestCase):
    def test_fetch_quote(self):
        adapter = QuoteApiAdapter()
        quote = adapter.fetch_quote()
        self.assertIsNotNone(quote)
        self.assertTrue(hasattr(quote, "content"))
        self.assertTrue(hasattr(quote, "author"))

if __name__ == "__main__":
    unittest.main()
