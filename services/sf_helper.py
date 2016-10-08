import requests

from settings import Settings
from logit import logit

logit('importing sf_helpers.py')

settings = Settings()

from logit import logit


class SfHelper:
    instance = None

    class __SfHelper:

        def __init__(self):
            self.sf_access = {}
            self.authorize()

        def authorize(self):
            logit('AUTHORIZING')
            credentials = {
                'grant_type': 'password',
                'client_id': settings.SALESFORCE['CONSUMER_KEY'],
                'client_secret': settings.SALESFORCE['CONSUMER_SECRET'],
                'username': settings.SALESFORCE['USERNAME'],
                'password': settings.SALESFORCE['PASSWORD'] + settings.SALESFORCE['SECURITY_TOKEN'],
                'request_uri': 'http://localhost'
            }

            response = requests.post(settings.SALESFORCE['LOGIN_URL'], credentials)
            if response.status_code == 200:
                logit('AUTHORIZE SUCCESS')
                self.sf_access = response.json()
            else:
                logit('AUTHORIZE FAIL, CODE: %d, RESPONSE: %s' % (response.status_code, response.content))
                self.sf_access = {}

        def test_access_token(self):
            headers = {
                'Authorization': 'Bearer ' + self.sf_access['access_token']
            }

            response = requests.get(settings.SALESFORCE['BASE_URL'] + '/services/data/v26.0/sobjects', headers=headers)
            if response.status_code == 200:
                logit('sf good', 'INFO')
            else:
                logit('sf bad', 'ERROR')

        def get_data(self, url, reauthorize=None):
            reauthorize = True if reauthorize is None else reauthorize
            headers = {'Authorization': 'Bearer ' + self.sf_access['access_token']}
            request_url = self.sf_access['instance_url'] + url
            response = requests.get(request_url, headers=headers)
            logit("URL: %s\nREAUTHORIZE: %s\nHEADERS: %s\nSTATUS_CODE: %d\nRESPONSE_CONTENT: %s\n" % (
            url, reauthorize, str(headers), response.status_code, str(response.content)))
            if response.status_code == 200:
                return response.json()
            elif response.content.index('INVALID_SESSION_ID') >=0 and reauthorize is True:
                logit('** REAUTHORIZING **')
                self.authorize()
                return self.get_data(url, False)
            else:
                return {'success': False}

    def __init__(self):
        if SfHelper.instance is None:
            SfHelper.instance = self.__SfHelper()
        else:
            pass

    def __getattr__(self, item):
        try:
            print('use existing instance attribute: %s' % repr(self.instance))
            return getattr(self.instance, item)
        except Exception as e:
            print('cannot access existing attribute on inner object: %s' % str(e))

    # def __getattr__(self, item):
    #     if self.instance is not None:
    #         return self.instance.settings[item]
    #     else:
    #         return None

    def __setattr__(self, item, value):
        try:
            print('use existing instance attribute: %s' % repr(self.instance))
            return setattr(self.instance, item, value)
        except Exception as e:
            print('cannot access existing attribute on inner object: %s' % str(e))

    # def __setattr__(self, key, value):
    #     if self.instance is not None:
    #         self.instance.settings[key] = value

    def get(self, item, default=None):
        if self.instance is not None:
            if item in self.instance.settings:
                return self.instance.settings[item]
            else:
                return default
        else:
            return default

    def set(self, key, value):
        if self.instance is not None:
            self.instance.settings[key] = value

    def get_dict(self):
        if self.instance is not None:
            return self.instance.settings


if __name__ == '__main__':
    sh = SfHelper()
    sh.test_access_token()
    url = "/services/data/v26.0/query/?q=select+Order_Id__c,+Name,+Tracking_Number__c,+Carrier__c,+Carrier_Link__c,+Status__c,+Scans__c+from+Shipment__c+where+Shipment_Number__C='S01001'"
    response = sh.get_data(url, True)
    pass
