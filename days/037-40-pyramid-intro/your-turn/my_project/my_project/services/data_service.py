import datetime
import random
from typing import List

from my_project.data import session_factory
from my_project.data.models.books import Book 


#def create_post(user: User, title:str, text:str, date: datetime.datetime, category: Category = None) -> Post:
#
#    session = session_factory.create_session()
#
#    post = Post()
#    post.author_id = user.id
#
#    if category is not None:
#        post.category_id = category.id
#
#    post.date = date
#    post.title = title
#    post.text = text
#
#    session.add(post)
#    session.commit()
#
#    return post


def get_book_by_id(book_id) -> List[Book]:
    session = session_factory.create_session()

    try:
        book = session.query(Book).filter(Book.id == book_id).first()
        return book

    finally:
        session.close()


def list_books() -> List[Book]:
    session = session_factory.create_session()

    try:
        posts = session.query(Book).all()
        return list(posts)

    finally:
        session.close()

