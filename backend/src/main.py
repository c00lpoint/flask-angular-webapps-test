from . import app
from .entities import Base, engine
from .routes import get_exams, add_exam
from .sample_utils import generate_sample_data

Base.metadata.create_all(engine)
generate_sample_data()

if __name__ == '__main__':

    # if needed, generate database schema
    app.run(debug=True)