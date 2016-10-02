import requests
from requests.auth import HTTPBasicAuth

from settings import Settings

settings = Settings()


def g(action, *args):
    url = settings.CARRIER['ENDPOINT'] + '/' + action
    for arg in args:
        if arg is not None:
            url += '/' + str(arg)
    r = requests.get(url,
                     auth=HTTPBasicAuth(settings.CARRIER['USERNAME'],
                                        settings.CARRIER['PASSWORD'])
                     )
    return r.json()


def CarrierHelper_which_carrier(tracking_number):
    return g('CarrierHelper_which_carrier', tracking_number)['return_value']


def CarrierHelper_track(tracking_number, carrier=None):
    return g('CarrierHelper_track', tracking_number, carrier)['return_value']


if __name__ == '__main__':
    pass
