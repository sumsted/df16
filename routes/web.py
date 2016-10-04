from bottle import static_file, route, get, post, template
from settings import Settings
from logit import logit

logit('importing web.py')

settings = Settings()


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=settings.DF16['STATIC_FOLDER'])


@get('/')
def get_index():
    return template('index.html')


@get('/enable')
def get_enable():
    # todo: generate skill access token that will be used by amazon
    # todo: present instructions and button to redirect to sf.com
    # todo: create new authorization row with data we have including the alexa access token that we generated
    return template('enable.html')


@post('/enable')
def post_enable():
    # todo: may not be used as we can get info from sf callback
    pass


@get('/callback')
def get_callback():
    # todo: get auth token and skill access token from request
    # todo: call salesforce to get salesforce access token
    # todo: store salesforce access token with alexa authorization row by alexa access token

    pass
