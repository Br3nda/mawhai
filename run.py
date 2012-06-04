
from bottle import route, run
from bottle import template

@route('/')
@route('/:name')
def index(name='World'):
    return template('default', name=name)

run(host='localhost', port=8080, reloader=True)

