from bottle import request, post

from logit import logit
from routes.alexa_handlers import handle_story_intent, handle_about_intent, handle_gary_intent, handle_dude_intent, \
    handle_help_intent, handle_session_end_request


@post('/alexa/event')
def post_alexa_event():
    result = {}
    alexa_event = request.json
    alexa_request = alexa_event['request'] if 'request' in alexa_event else None
    alexa_session = alexa_event['session'] if 'session' in alexa_event else None
    logit('alexa_event: %s' % str(alexa_event))

    # todo add check
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if alexa_event['session']['new']:
        logit('New Session: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))
    if alexa_event['request']['type'] == "LaunchRequest":
        logit('LaunchRequest: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))
        return {"welcome"}
    elif alexa_event['request']['type'] == "IntentRequest":
        logit('IntentRequest: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))
        return route_intent(alexa_request, alexa_session)
    elif alexa_event['request']['type'] == "SessionEndedRequest":
        logit('SessionEndedRequest: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))
    return result


def route_intent(alexa_request, alexa_session):
    intent = alexa_request['intent']
    intent_name = alexa_request['intent']['name']

    if intent_name in ["storyIntent"]:
        return handle_story_intent(intent, alexa_session)
    elif intent_name in ["aboutIntent"]:
        return handle_about_intent(intent, alexa_session)
    elif intent_name in ["garyIntent"]:
        return handle_gary_intent(intent, alexa_session)
    elif intent_name in ["dudeIntent"]:
        return handle_dude_intent(intent, alexa_session)
    elif intent_name in ["AMAZON.HelpIntent", "helpIntent"]:
        return handle_help_intent()
    elif intent_name in ["AMAZON.CancelIntent", "AMAZON.StopIntent", 'quitIntent']:
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")
