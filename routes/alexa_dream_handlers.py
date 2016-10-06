from dream.dream import get_help, gary, dude, get_shipment, get_shipment_by_order
from logit import logit


def get_access_token(alexa_session):
    try:
        return alexa_session['user']['accessToken']
    except:
        return ''


def get_slot(intent, key, default=None):
    try:
        return intent['slots'][key]['value']
    except:
        return default


def build_speechlet_response(title, speech_output, reprompt_text, should_end_session, card_output=None):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': speech_output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': card_output or speech_output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def handle_gary_intent(intent, session):
    session_attributes = {}
    card_title = "Gary?"

    speech_output = gary()

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def handle_dude_intent(intent, session):
    session_attributes = {}
    card_title = "I'm the dude!"

    speech_output = dude()

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def handle_help_intent():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome to Memphis"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hey are you there? Astro waits for no one. What would you like to do?"

    help = get_help()

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, help, reprompt_text, should_end_session, help))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for visiting Memphis. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def handle_about_intent(intent, session):
    title = "#DF16 - About"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm talking about "
    reprompt_text = None
    try:
        item_number = get_slot(intent, 'item', '')
        speech_output += item_number
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_story_intent(intent, session):
    title = "#DF16 - Story"
    should_end_session = False
    session_attributes = {}
    speech_output = "Once upon a time, "
    reprompt_text = None
    try:
        speech_output += 'ugh, do you really want to hear a story?'
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_shipment_intent(intent, session):
    title = "#DF16 - Order"
    should_end_session = False
    session_attributes = {}
    speech_output = ""
    reprompt_text = None
    try:
        speech_output = get_shipment()
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_order_intent(intent, session):
    title = "#DF16 - Order"
    should_end_session = False
    session_attributes = {}
    speech_output = ""
    reprompt_text = None
    try:
        order_id = get_slot(intent, 'order_id', '')
        order_id_str = ("00000000%d"%order_id)[-8:]
        speech_output = get_shipment_by_order(order_id_str)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))
