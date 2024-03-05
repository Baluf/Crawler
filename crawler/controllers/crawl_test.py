import unittest
from unittest.mock import patch
from server import app


class TestCrawlEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('facade.crawl_facade.CrawlFacade.create_crawl')
    @patch('facade.crawl_facade.CrawlFacade.crawl_page')
    def test_crawl_endpoint_success(self, mock_crawl_page, mock_create_crawl):
        mock_create_crawl.return_value = "4bbb71f3-8ac1-4d28-83d3-e673e996d993"  # Simulate successful crawl creation
        payload = {'url': 'http://google.com', 'notify': 0}
        response = self.app.post('/crawl', json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(mock_create_crawl.called)
        mock_crawl_page.assert_called_once()

    @patch('facade.crawl_facade.CrawlFacade.create_crawl')
    @patch('facade.crawl_facade.CrawlFacade.crawl_page')
    def test_crawl_endpoint_failed(self, mock_crawl_page, mock_create_crawl):
        mock_create_crawl.return_value = "4bbb71f3-8ac1-4d28-83d3-e673e996d993"  # Simulate successful crawl creation
        payload = {'url': 'badschema-google.com', 'notify': 0}
        response = self.app.post('/crawl', json=payload)

        self.assertEqual(response.status_code, 400)

