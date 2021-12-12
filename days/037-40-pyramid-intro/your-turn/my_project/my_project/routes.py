def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('list_books', '/books/')
    config.add_route('details', '/book/{book_id}')
#    config.add_route('add_book', '/add_book/')
