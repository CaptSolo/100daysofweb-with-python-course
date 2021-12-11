import datetime
import random
from typing import List

from data import session_factory
from data.models.users import User
from data.models.posts import Post
from data.models.categories import Category


def get_default_user():
    session = session_factory.create_session()

    user = session.query(User).filter(User.email == 'user1@example.org').first()
    if user:
        return user

    user = User()
    user.email = 'user1@example.org'
    user.name = 'Pirmais lietotājs'
    session.add(user)

    session.commit()

    return user


def get_category(name: str) -> Category:

    session = session_factory.create_session()

    cat = session.query(Category).filter(Category.name == name).first()

    session.commit()

    return cat


def create_post(user: User, title:str, text:str, date: datetime.datetime, category: Category = None) -> Post:

    session = session_factory.create_session()

    post = Post()
    post.author_id = user.id

    if category is not None:
        post.category_id = category.id

    post.date = date
    post.title = title
    post.text = text

    session.add(post)
    session.commit()

    return post


def list_posts() -> List[Post]:
    session = session_factory.create_session()

    # noinspection PyComparisonWithNone
    posts = session.query(Post).all()

    return list(posts)


