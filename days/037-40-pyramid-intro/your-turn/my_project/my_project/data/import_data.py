import datetime
import random

from my_project.data import session_factory
from my_project.data.models.books import Book
#from services import data_service


def import_if_empty():
    __import_books()


def __import_books():
    session = session_factory.create_session()
    if session.query(Book).count() > 0:
        return

    book1 = Book()
    book1.title = 'Hello, world!'
    book1.author = 'Douglas Adams'
    book1.date = datetime.datetime.now()

    session.add(book1)

    book2 = Book()
    book2.title = 'All you need to know'
    book2.author = 'Anonymous Wizard'
    book2.date = datetime.datetime.now()

    session.add(book2)

    # ToDo = add some more books

    session.commit()


