from bottle import static_file, route, get, post, template

from logit import logit
from services.sf_helper import SfHelper
from settings import Settings

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


@get('/df/shipment/<email_address>/<shipment_id>')
def get_shipment(email_address, shipment_id):
    # todo : call a bunch of sf here
    shipments = {
        'shipments': [
        ]
    }
    url = "/services/data/v37.0/query/?q=select+Shipment_Number__c,+Name,+Tracking_Number__c,+Carrier__c,+Carrier_Link__c,+Status__c,+Scans__c+from+Shipment__c+where+Shipment_Number__C='%s'" % shipment_id

    sh = SfHelper()
    try:
        sf_objects = sh.get_data(url)
        for sf_object in sf_objects['records']:
            shipments['shipments'].append(sf_object)
    except Exception as e:
        logit('problem getting shipment for %s, %s'%(email_address, shipment_id))
    return shipments
