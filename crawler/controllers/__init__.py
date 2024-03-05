from flask import Blueprint

crawls_blueprint = Blueprint('crawls_blueprint', __name__)

from . import crawl_controller
