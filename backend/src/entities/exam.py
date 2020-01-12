from sqlalchemy import Column, String

from .entity import Entity, Base


class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, desciption, create_by):
        Entity.__init__(self, create_by)
        self.title = title
        self.description = desciption
