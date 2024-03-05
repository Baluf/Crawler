from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import engine

Base = declarative_base()


class Crawl(Base):
    __tablename__ = 'crawls'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String)
    status = Column(String)
    html_file_path = Column(String)

    def __repr__(self):
        return "<Crawl(crawl_id='%s', url='%s', status='%s', html_file_path='%s')>" % (
            self.id, self.url, self.status, self.html_file_path
        )


Base.metadata.create_all(engine)
