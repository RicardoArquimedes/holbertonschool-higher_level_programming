#!/usr/bin/python3
"""Start link class to table in database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select


if __name__ == "__main__":

    connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'. \
        format(argv[1], argv[2], argv[3])

    engine = create_engine(connect, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%')).all()

    for row in query:
        print("{}: {}".format(row.id, row.name))

    session.close()