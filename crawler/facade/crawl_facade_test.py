import unittest
from unittest.mock import patch, MagicMock
from facade.crawl_facade import CrawlFacade


class TestCrawlFacade(unittest.TestCase):
    @patch('facade.crawl_facade.CrawlDao')
    @patch('facade.crawl_facade.requests')
    @patch('facade.crawl_facade.threading')
    def test_crawl_page_success(self, mock_threading, mock_requests, mock_crawl_dao):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><body><h1>Mock HTML</h1></body></html>'
        mock_requests.get.return_value = mock_response

        mock_crawl_dao_instance = MagicMock()
        mock_crawl_dao.return_value = mock_crawl_dao_instance

        CrawlFacade.crawl_page('d48e7d91-87ac-4024-abb1-942e882d01af', 'http://example.com', notify=0)

        mock_threading.Thread.assert_called_once_with(target=CrawlFacade.notify_user, args=('d48e7d91-87ac-4024-abb1-942e882d01af', 0))

    @patch('facade.crawl_facade.CrawlDao')
    @patch('facade.crawl_facade.requests')
    @patch('facade.crawl_facade.threading')
    def test_crawl_page_failure(self, mock_threading, mock_requests, mock_crawl_dao):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = '<html><body><h1>Mock HTML</h1></body></html>'
        mock_requests.get.return_value = mock_response

        mock_crawl_dao_instance = MagicMock()
        mock_crawl_dao.return_value = mock_crawl_dao_instance

        CrawlFacade.crawl_page('d48e7d91-87ac-4024-abb1-942e882d01af', 'http://example.com', notify=0)
        mock_threading.Thread.assert_not_called()


if __name__ == '__main__':
    unittest.main()