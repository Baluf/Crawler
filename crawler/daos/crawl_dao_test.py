import unittest
from unittest.mock import patch, MagicMock
from daos.crawl_dao import CrawlDao
from database.schema import Crawl
from dtos.crawl_dto import CrawlDto


class TestCrawlDao(unittest.TestCase):
    @patch('daos.crawl_dao.Session')
    def setUp(self, mock_session):
        self.dao = CrawlDao()
        self.mock_session = mock_session

    def test_insert_crawl(self):
        mock_session_instance = MagicMock()
        self.mock_session.return_value = mock_session_instance

        crawl_id = "d48e7d91-87ac-4024-abb1-942e882d01as"
        url = 'http://example.com'
        status = 'ACCEPTED'

        returned_id = "d48e7d91-87ac-4024-abb1-942e882d01as"
        mock_session_instance.commit.return_value = returned_id

        result = insert_crawl(crawl_id, url, status)

        self.assertEqual(result, returned_id)
        mock_session_instance.add.assert_called_once()
        mock_session_instance.commit.assert_called_once()

    def test_update_crawl(self):
        mock_session_instance = MagicMock()
        self.mock_session.return_value = mock_session_instance

        crawl_id = "d48e7d91-87ac-4024-abb1-942e882d01as"
        html_file_path = '/path/to/html'
        status = 'COMPLETED'

        self.dao.update_crawl(crawl_id, html_file_path, status)

        mock_session_instance.query.assert_called_once_with(Crawl)
        mock_session_instance.query.return_value.filter_by.assert_called_once_with(id=crawl_id)
        mock_session_instance.query.return_value.filter_by.return_value.first.assert_called_once()
        mock_session_instance.commit.assert_called_once()

    def test_get_crawl_by_id(self):
        mock_session_instance = MagicMock()
        self.mock_session.return_value = mock_session_instance

        crawl_id = "d48e7d91-87ac-4024-abb1-942e882d01as"
        expected_crawl_dto = CrawlDto(crawl_id, 'http://example.com', 'COMPLETED', '/path/to/html')
        mock_crawl = MagicMock(id=crawl_id, url='http://example.com', status='COMPLETED', html_file_path='/path/to/html')
        mock_session_instance.query.return_value.filter_by.return_value.first.return_value = mock_crawl

        result = self.dao.get_crawl_by_id(crawl_id)

        self.assertEqual(result.crawl_id, expected_crawl_dto.crawl_id)
        self.assertEqual(result.url, expected_crawl_dto.url)
        self.assertEqual(result.status, expected_crawl_dto.status)
        self.assertEqual(result.html_file_path, expected_crawl_dto.html_file_path)


if __name__ == '__main__':
    unittest.main()