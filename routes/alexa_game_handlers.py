from game.game import get_help, gary, dude, attack, go, look_around, take, health, eat, look_direction
from game.player import Player
from logit import logit

player = Player("Nicholas")


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
    card_title = "Welcome to Dreamland"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hey are you there? Dreamland waits for no one. What would you like to do?"

    help = get_help()

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, help[0], reprompt_text, should_end_session, help[1]))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for visiting Dreamland. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def handle_attack_intent(intent, session):
    title = "Dreamland - ATTACK!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm attacking."
    reprompt_text = None
    try:
        item_name = get_slot(intent, 'item', '')
        speech_output = attack(player, item_name)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_navigate_intent(intent, session):
    title = "Dreamland - RUN!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm running."
    reprompt_text = None
    try:
        direction = get_slot(intent, 'direction', '')
        speech_output = go(player, direction)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_look_direction_intent(intent, session):
    title = "Dreamland - LOOKING!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm looking."
    reprompt_text = None
    try:
        direction = get_slot(intent, 'direction', '')
        speech_output = look_direction(player.location, direction)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_look_intent(intent, session):
    title = "Dreamland - LOOKING!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm looking around."
    reprompt_text = None
    try:
        speech_output = look_around(player)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_take_intent(intent, session):
    title = "Dreamland - TAKING!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm taking stuff."
    reprompt_text = None
    try:
        item_name = get_slot(intent, 'item', '')
        speech_output = take(player, item_name)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_health_intent(intent, session):
    title = "Dreamland - HEALTH!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm healthy."
    reprompt_text = None
    try:
        speech_output = health(player)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_eat_intent(intent, session):
    title = "Dreamland - EAT!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm eating."
    reprompt_text = None
    try:
        item_name = get_slot(intent, 'item', '')
        speech_output = eat(player, item_name)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_restart_intent(intent, session):
    title = "Dreamland - RESTART!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm restarting."
    reprompt_text = None
    try:
        pass
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_play_intent(intent, session):
    title = "Dreamland - Welcome!"
    should_end_session = False
    session_attributes = {}
    speech_output = "Welcome to Dreamland. Home of the sales, land of the service. "
    reprompt_text = None
    try:
        speech_output += look_around(player)
        speech_output += health(player)
    except Exception as e:
        logit(str(e), 'ERROR')
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))
