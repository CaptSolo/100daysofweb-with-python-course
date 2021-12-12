from pyramid.config import Configurator
import os

#from my_project.bin import load_base_data
#from my_project.data.db_session import DbSession

from my_project.data import session_factory
from my_project.data import import_data


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.scan()

    init_db()

    return config.make_wsgi_app()


def init_db():
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'db',
        'books.sqlite'
    )
    session_factory.global_init(db_file)
    session_factory.create_tables()
    import_data.import_if_empty()
    #load_base_data.load_starter_data()

