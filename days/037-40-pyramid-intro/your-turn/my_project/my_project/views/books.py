from pyramid.view import view_config
from pyramid.response import Response

from my_project.services import data_service


@view_config(route_name='list_books', renderer='my_project:templates/books.pt')
def my_view(request):

    books = data_service.list_books() 

    return {'books': books}


@view_config(route_name='details', renderer='my_project:templates/book_info.pt')
def book_view(request):

    book_id = int(request.matchdict.get('book_id'))
    book = data_service.get_book_by_id(book_id)

    if not book:
        return Response(status=404)

    return {'book': book}


#@view_config(route_name='add_book', renderer='my_project:templates/book_info.pt')
#def add_book_view(request):
#
#    book_id = int(request.matchdict.get('book_id'))
#    book = data_service.get_book_by_id(book_id)
#
#    if not book:
#        return Response(status=404)
#
#    return {'book': book}

