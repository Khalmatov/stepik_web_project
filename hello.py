def wsgi_application(environ, start_responce):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    data = environ['QUERY_STRING'].split('&')
    body = '\n'.join(data).encode('utf-8')
    start_responce(status, headers)
    return [body]
