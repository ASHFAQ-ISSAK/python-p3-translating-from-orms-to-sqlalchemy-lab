import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Dog

db_dir = "dogs.db"
SQLITE_URL = f"sqlite:///{db_dir}"


def create_table(base, engine):
    base.metadata.create_all(engine)


def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()


def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    return session.query(Dog).all()


def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()


if __name__ == "__main__":
    engine = create_engine(SQLITE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    # Example usage
    dog = Dog(name="joey", breed="cocker spaniel")
    save(session, dog)

    retrieved_dog = find_by_name(session, "joey")
    if retrieved_dog:
        print(f"Retrieved dog: {retrieved_dog.name} - {retrieved_dog.breed}")
    else:
        print("Dog not found")

    os.remove(db_dir)
