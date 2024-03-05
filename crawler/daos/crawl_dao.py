from database.schema import Crawl
from database import Session
from dtos.crawl_dto import CrawlDto

class CrawlDao:

    def __init__(self):
        pass

    def insert_crawl(self, crawl_id, url, status):
        """
        Insert facade by crawl_id
        :param crawl_id
        :param url
        :param status
        """
        session = Session()
        try:
            crawl = Crawl(id=crawl_id, url=url, status=status)
            session.add(crawl)
            session.commit()
            return crawl_id

        except Exception as e:
            print("Error insert_crawl_into_db:", e)
            session.rollback()
            return

        finally:
            session.close()

    def update_crawl(self, crawl_id, html_file_path, status):
        """
        Update facade by crawl_id
        :param crawl_id
        :param html_file_path
        :param status
        """
        session = Session()

        try:
            crawl = session.query(Crawl).filter_by(id=crawl_id).first()
            crawl.status = status

            if html_file_path:
                crawl.html_file_path = html_file_path
            session.commit()

        except Exception as e:
            print("Error fetching facade:", e)
            session.rollback()

        finally:
            session.close()

    def get_crawl_by_id(self, crawl_id):
        """
        Get facade by crawl_id
        :param crawl_id
        :return facade instance from db
        """
        session = Session()

        try:
            crawl = session.query(Crawl).filter_by(id=crawl_id).first()
            return CrawlDto(crawl.id, crawl.url, crawl.status, crawl.html_file_path)
        except Exception as e:
            print("Error fetching facade:", e)
            return None

        finally:
            session.close()
