from pyramid.view import view_config


@view_config(route_name='home', renderer='my_project:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'My Project'}
