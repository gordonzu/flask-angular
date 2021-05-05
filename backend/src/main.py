from .entities.entity import Session, engine, Base
from .entities.exam import Exam

Base.metadata.create_all(engine)
session = Session()
exams = session.query(Exam).all()

if len(exams) == 0:
    python_exam = Exam("SQLAlchemy Exam", "Test your knowledge of SQLAlchemy.", "script")
    session.add(python_exam)
    session.commit()
    session.close()

    exams = session.query(Exam).all()

    print('#### Exams: ')
    for exam in exams:
        print(f'({exam.id}) {exam.title} - {exam.description}')


