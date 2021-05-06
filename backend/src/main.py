from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema

app = Flask(__name__)

Base.metadata.create_all(engine)

@app_route('/exams')
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()

    schema = Exam Schema(many=True)
    exams = schema.dump(exam_objects)

    session.close()
    return jsonify(exams.data)

@app_route('/exams', methods=['POST'])
def add_exam():
    posted_exam = ExamSchema(only=('title', 'description'))\
            .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    session = Session()
    session.add(exam)
    session.commit()

    new_exam = ExamSchema().dump(exam).data

    session.close()
    return jsonify(new_exam), 201



if len(exams) == 0:
    python_exam = Exam("SQLAlchemy Exam", "Test your knowledge of SQLAlchemy.", "script")
    session.add(python_exam)
    session.commit()

    exams = session.query(Exam).all()

    print('#### Exams: ')
    for exam in exams:
        print(f'({exam.id}) {exam.title} - {exam.description}')


