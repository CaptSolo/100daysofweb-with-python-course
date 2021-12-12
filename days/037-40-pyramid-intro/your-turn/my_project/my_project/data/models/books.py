import datetime

import sqlalchemy as sa
from sqlalchemy import orm

from my_project.data.sqlalchemybase import SqlAlchemyBase


class Book(SqlAlchemyBase):
    __tablename__ = "books"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    date_added = sa.Column(sa.DateTime, default=datetime.datetime.now)
    title = sa.Column(sa.String, index=True)
    author = sa.Column(sa.String, index=True)

    #author_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    #author = orm.relation("User")

    #category_id = sa.Column(sa.Integer, sa.ForeignKey('categories.id'))
    #category = orm.relation("Category")
    
