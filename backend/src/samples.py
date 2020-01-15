from .entities import Base, engine, Session
from .entities.exam import Exam


def generate_sample_data():

    session = Session()
    exams = session.query(Exam).all()

    if len(exams) == 0:
        # create and persist dummy exam
        python_exam = Exam('SQLAlchemy Exam', 'Test your knowledge about SQLAlchemy', 'script')
        session.add(python_exam)
        session.commit()
        session.close()

    # reload exams
    # exams = session.query(Exam).all()
    # print('### Exams:')
    # for exam in exams:
    #     print(f'({exam.id}) {exam.title} - {exam.description}')





