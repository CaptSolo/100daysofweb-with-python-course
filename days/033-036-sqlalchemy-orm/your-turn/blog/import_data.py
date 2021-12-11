import datetime
import random

from data import session_factory
from data.models.users import User
from data.models.posts import Post
from data.models.categories import Category
#from services import data_service


def import_if_empty():
    __import_users()
    __import_categories()
    __import_posts()


def __import_users():
    session = session_factory.create_session()
    if session.query(User).count() > 0:
        return

    # TODO - add this!
    #data_service.get_default_user()

    user1 = User()
    user1.email = 'user1@example.org'
    user1.name = 'Pirmais lietotājs'
    session.add(user1)
    session.commit()


def __import_categories():
    session = session_factory.create_session()
    if session.query(Category).count() > 0:
        return

    cat1 = Category()
    cat1.name = 'Semantic Web'
    session.add(cat1)

    cat2 = Category()
    cat2.name = 'General'
    session.add(cat2)

    session.commit()


def __import_posts():
    session = session_factory.create_session()
    if session.query(Post).count() > 0:
        return

    user = session.query(User).filter(User.email == 'user1@example.org').one()

    post1 = Post()
    post1.title = 'Hello, world!'
    post1.date = datetime.datetime.now()
    post1.text = """Hello, world!


This is my first blog post.
"""

    post1.author_id = user.id

    # ToDo:
    #  - must add category.id and author.id
    session.add(post1)

    # ToDo = add some more posts

    session.commit()


