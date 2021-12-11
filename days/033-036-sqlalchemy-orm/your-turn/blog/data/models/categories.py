import sqlalchemy as sa
from sqlalchemy import orm

from data.models.posts import Post
from data.sqlalchemybase import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = "categories"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name =  sa.Column(sa.String, index=True, nullable=True)

    posts = orm.relation("Post", order_by=[Post.date.desc(),], back_populates="category")

