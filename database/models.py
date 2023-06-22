from sqlalchemy import Column, String, Integer

from database.connect import Base


class Image(Base):
    __tablename__ = 'Image'

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer)
    name = Column(String)
    tag = Column(String)
    size = Column(Integer)
    mime_type = Column(String)
    modification_time = Column(String)
