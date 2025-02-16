

import import_data
from data import session_factory
from data.models.users import User
from data.models.categories import Category
#from infrastructure.numbers import try_int
#from infrastructure.switchlang import switch
from services import data_service

from datetime import datetime

from sqlalchemy import select

user: User = None


def print_post_list():

    posts = data_service.list_posts()

    for post in posts:

        cat_name = post.category.name if (post.category is not None) else None
 
        print(f"{post.id}: {post.title}")

        print(f"  Author:   {post.author.name}")
        print(f"  Created:  {post.date}")
        print(f"  Category: {cat_name}")

        print()
        print(post.text)
        print("---\n")


def add_new_post():

    user = data_service.get_default_user()

    cat = data_service.get_category("Semantic Web")

    title = "Second post"
    text = """\
This is the second post.

It was created in program.py.
"""

    now = datetime.now()

    new_post = data_service.create_post(user, title, text, now, cat)


def main():
    setup_db()

    print_post_list()

    add_new_post()

    print_post_list()


def setup_db():
    global user
    session_factory.global_init('blog_posts.sqlite')
    session_factory.create_tables()
    import_data.import_if_empty()
    # user = data_service.get_default_user()


if __name__ == '__main__':
    main()

