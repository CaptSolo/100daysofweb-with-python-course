import datetime
import sqlalchemy as sa
from sqlalchemy import orm

from data.models.posts import Post
from data.sqlalchemybase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, nullable=True)

    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    posts = orm.relation("Post", order_by=[Post.date.desc(),], back_populates="author")
