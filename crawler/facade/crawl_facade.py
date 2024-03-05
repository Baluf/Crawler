import os
import threading
from http import HTTPStatus

from constants import CrawlStatuses, HTML_FILES_DIR
from daos.crawl_dao import CrawlDao
import requests

from notifiers.notifiers import *

os.makedirs(HTML_FILES_DIR, exist_ok=True)


class CrawlFacade:
    CRAWL_DAO = CrawlDao()

    @classmethod
    def get_crawl(cls, crawl_id):
        return cls.CRAWL_DAO.get_crawl_by_id(crawl_id)

    @classmethod
    def create_crawl(cls, crawl_id, url, status):
        return cls.CRAWL_DAO.insert_crawl(crawl_id, url, status)

    @staticmethod
    def notify_user(crawl_id, notify):
        notifiers = [SlackChannelNotifier(), SlackUserNotifier(), EmailNotifier()]
        message = f"facade id -> {crawl_id} completed!"

        if notify == 0:
            for notifier in notifiers:
                notifier.send_message(message)
        elif notify in range(1, len(notifiers) + 1):
            notifiers[notify - 1].send_message(message)
        else:
            print("Invalid notification option. Please choose between 0 and", len(notifiers))
            print("0 - For all notifiers")
            for i, notifier in enumerate(notifiers, start=1):
                print(f"{i} - For {notifier.__class__.__name__}")

    @staticmethod
    def crawl_page(crawl_id, url, notify):
        CrawlFacade.CRAWL_DAO.update_crawl(crawl_id, None, CrawlStatuses.RUNNING)
        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK:
                html_content = response.text
                html_file_path = os.path.join(HTML_FILES_DIR, f"{crawl_id}.html")
                with open(html_file_path, 'w') as f:
                    f.write(html_content)
                CrawlFacade.CRAWL_DAO.update_crawl(crawl_id, html_file_path, CrawlStatuses.COMPLETE)
                threading.Thread(target=CrawlFacade.notify_user, args=(crawl_id, notify)).start()

            else:
                CrawlFacade.CRAWL_DAO.update_crawl(crawl_id, None, CrawlStatuses.ERROR)

        except Exception as e:
            print("Error occurred during facade:", e)
            CrawlFacade.CRAWL_DAO.update_crawl(crawl_id, None, CrawlStatuses.ERROR)