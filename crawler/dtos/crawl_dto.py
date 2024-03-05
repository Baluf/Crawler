class CrawlDto(object):

    def __init__(self, crawl_id, url, status, html_file_path):
        self._crawl_id = crawl_id
        self._url = url
        self._status = status
        self._html_file_path = html_file_path

    @property
    def crawl_id(self):
        return self._crawl_id

    @crawl_id.setter
    def crawl_id(self, value):
        self._crawl_id = value.upper()

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value.upper()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value.upper()

    @property
    def html_file_path(self):
        return self._html_file_path

    @html_file_path.setter
    def html_file_path(self, value):
        self._html_file_path = value.upper()
