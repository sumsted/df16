
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
            credentials = {
                'grant_type': 'password',
                'client_id': settings.SALESFORCE['CONSUMER_KEY'],
                'client_secret': settings.SALESFORCE['CONSUMER_SECRET'],
                'username': settings.SALESFORCE['USERNAME'],
                'password': settings.SALESFORCE['PASSWORD']+settings.SALESFORCE['SECURITY_TOKEN'],
                'request_uri': 'http://localhost'
            }

            response = requests.post(settings.SALESFORCE['LOGIN_URL'], credentials)
            if response.status_code == 200:
                self.sf_access = response.json()
                logit('it worked'+str(self.sf_access))
            else:
                self.sf_access = {}
                logit('it failed')

        def test_access_token(self, res):
            headers = {
                'Authorization': 'Bearer' + self.sf_access['access_token']
            }

            response = requests.get(settings.SALESFORCE['BASE_URL']+'/services/data/v26.0sobjects', headers=headers)
            if response.status_code == 200:
                logit('sf good', 'INFO')
            else:
                logit('sf bad', 'ERROR')

        def get_data(self, options, reauthorize=None):
            reauthorize = True if reauthorize is None else False
            options['headers'] = {'Authorization': 'Bearer ' + self.sf_access['access_token']}
            response = requests.get(options['url'])
            if response.status_code == 200:
                return response.json()
            elif 'INVALID_SESSION_ID' in response.content and reauthorize is True:
                self.authorize()
                return self.get_data(options, False)
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


if __name__=='__main__':
    sh = SfHelper()
    pass
