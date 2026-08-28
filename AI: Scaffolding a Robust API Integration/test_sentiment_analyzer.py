import os
from unittest.mock import patch

from sentiment_analyzer import analyze_sentiment


class MockResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {"label": "pos"}


def mock_post(url, data, headers):
    print(f"Authorization header: {headers['Authorization']}")
    return MockResponse()


os.environ["TEXT_PROCESSING_API_KEY"] = "DUMMY_KEY"

with patch("sentiment_analyzer.requests.post", side_effect=mock_post):
    result = analyze_sentiment("I love this product")

print(f"Sentiment result: {result}")

