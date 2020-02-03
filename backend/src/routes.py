from flask import jsonify, request

from . import app
from .entities import Session
from .entities.exam import Exam
from .schemas.exam import ExamSchema
from .contextmgrs import open_session


@app.route('/get-exams')
def get_exams():

    with open_session(Session) as session:
        # fetching from database
        exam_objects = session.query(Exam).all()

        # transforming into JSON-serializable objects
        schema = ExamSchema(many=True)
        exams = schema.dump(exam_objects)

    # serializing as JSON
    return jsonify(exams)


@app.route('/add-exam', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description')).load(request.get_json())

    exam = Exam(**posted_exam, create_by='HTTP post request')

    with open_session(Session) as session:
        # persist exam
        session.add(exam)
        session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam)
    return jsonify(new_exam), 201

