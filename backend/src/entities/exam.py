from sqlalchemy import Column, String

from . import Base
from .entity import Entity


class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, create_by):
        Entity.__init__(self, create_by)
        self.title = title
        self.description = description
