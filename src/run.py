
from bottle import route, run, static_file, template 

@route('/')
def index():
    return template('index')

@route('/<path:path>')
def callback(path):
    print path
    return static_file(path, root='/home/brenda/projects/mawhai/www/')

run(host='localhost', port=8080, reloader=True)

