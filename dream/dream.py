from logit import logit
from services.sf_helper import SfHelper


def dude():
    """dude
    You can add your own funny commands.
    Just create a function and call it from the do_command() if statement
    """
    return "I know what dude I am! I'm the dude, playing a dude, disguised as another dude!"


def gary():
    """gary
    Another funny command.
    """
    return "Gary? Gary? pfpfpfpfppff    pfpfpfpfppff Gary? Guys, I can't find Gary."


def get_help():
    """help
    Add commands to this or leave them off to make them secret.
    """
    return "Welcome to Dreamland. May the trail force be with you."


def get_shipment():
    speech = ""
    url = "/services/data/v37.0/query/?q=select+Shipment_Number__c,+Name,+Tracking_Number__c,+Carrier__c,+Carrier_Link__c,+Status__c,+Scans__c+from+Shipment__c"
    sh = SfHelper()
    try:
        sf_objects = sh.get_data(url)
        count = len(sf_objects['records'])
        if count == 0:
            speech = "You have no orders. "
        elif count == 1:
            speech = "You have one order. "
        elif count > 1:
            speech = "You have %d orders. " % count
        for i, sf_object in enumerate(sf_objects['records']):
            if count == 1:
                speech = "Your %s is being delivered by %s and has a shipment status of %s. " % (i, sf_object['Name'], sf_object['Carrier__c'], sf_object['Status__c'])
            else:
                verb = "are" if sf_object['Name'][-1] == "s" else "is"
                speech += "Shipment %d %s a %s, is being delivered by %s and has a shipment status of %s. " % (i+1, verb, sf_object['Name'], sf_object['Carrier__c'], sf_object['Status__c'])
    except Exception as e:
        logit('problem getting shipment')
        speech = "There was a problem pulling your shipments"
    return speech
