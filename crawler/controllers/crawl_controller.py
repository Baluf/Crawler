from flask import request, jsonify

from constants import CrawlStatuses
import threading
import uuid
from http import HTTPStatus

from facade.crawl_facade import CrawlFacade
from utils.validations import is_valid_uuid, is_url

from . import crawls_blueprint


@crawls_blueprint.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()

    url = data.get('url')

    if not is_url(url):
        return jsonify({'error': 'url is not valid'}), HTTPStatus.BAD_REQUEST

    notify = data.get('notify') if data.get('notify') else 0
    crawl_id = str(uuid.uuid4())

    created_crawl_id = CrawlFacade.create_crawl(crawl_id=crawl_id, url=url, status=CrawlStatuses.ACCEPTED)
    threading.Thread(target=CrawlFacade.crawl_page, args=(crawl_id, url, notify)).start()

    if created_crawl_id:
        return jsonify({'crawl_id': crawl_id}), HTTPStatus.CREATED
    else:
        return jsonify({'error': 'Crawl ID creation operation failed'}), HTTPStatus.BAD_REQUEST


@crawls_blueprint.route('/crawl/status/<crawl_id>', methods=['GET'])
def status(crawl_id):
    if not is_valid_uuid(crawl_id):
        return jsonify({'error': 'Crawl ID is not valid'}), HTTPStatus.BAD_REQUEST

    selected_crawl = CrawlFacade.get_crawl(crawl_id)
    if selected_crawl:
        return jsonify({'status': selected_crawl.status}), HTTPStatus.OK
    else:
        return jsonify({'error': 'Crawl ID not found'}), HTTPStatus.NOT_FOUND
