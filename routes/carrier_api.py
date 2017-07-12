from bottle import get

from carrier.CarrierHelper_client import CarrierHelper_track, CarrierHelper_which_carrier


@get('/track/<tracking_number>')
def get_shipment(tracking_number):
    return CarrierHelper_track(tracking_number)


@get('/carrier/<tracking_number>')
def get_carrier(tracking_number):
    try:
        response = {'success': True, 'carrier': CarrierHelper_which_carrier(tracking_number)[0]}
    except Exception as e:
        response = {'success': False}
    return response


@get('/account/<account_number>')
def get_account(account_number):
    result = {'success': True, 'tracks': ['779604161320', '787117332275', '622448465873']}
    return result
