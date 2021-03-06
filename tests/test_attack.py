from unittest import TestCase

import requests


class TestAttack(TestCase):
    URL = "http://localhost:8085/alexa/event"

    def test_east(self):
        take_request = {
            "session": {
                "sessionId": "amzn1.echo-api.session.c398c68a-7578-41d2-91f2-fe12b670f679",
                "user": {
                    "userId": "amzn1.ask.account.AEEJPMHKHF2DINXCST2H3GAKEG5H5V2JCO6WH5PULVUYQ7PHPDNC2I6VORS4FG2YJ3TJDUOCCFWZYVBDIRHAINSQG2MRVZKJMA7GY3SKGPUHR6ZRQAFGXD5FMOKBFVJWHF4YSYBJBPIWUP76LLSW47AC6JUVPO4Q3QDMYBGRUXWNHUID73T4L54HUHPYEJESTNKP24XHXYUQVVY"
                },
                "new": False,
                "application": {
                    "applicationId": "amzn1.ask.skill.ceccea0b-f170-4541-b01c-a054a9a5676b"
                }
            },
            "version": "1.0",
            "request": {
                "intent": {
                    "slots": {
                        "item": {
                            "value": "spoon",
                            "name": "item"
                        }
                    },
                    "name": "takeIntent"
                },
                "locale": "en-US",
                "requestId": "amzn1.echo-api.request.cda5a835-a17e-4803-83ef-e3d64bcbd567",
                "type": "IntentRequest",
                "timestamp": "2016-09-25T01:10:47Z"
            },
            "context": {
                "AudioPlayer": {
                    "playerActivity": "IDLE"
                },
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.ceccea0b-f170-4541-b01c-a054a9a5676b"
                    },
                    "device": {
                        "supportedInterfaces": {
                            "AudioPlayer": {}
                        }
                    },
                    "user": {
                        "userId": "amzn1.ask.account.AEEJPMHKHF2DINXCST2H3GAKEG5H5V2JCO6WH5PULVUYQ7PHPDNC2I6VORS4FG2YJ3TJDUOCCFWZYVBDIRHAINSQG2MRVZKJMA7GY3SKGPUHR6ZRQAFGXD5FMOKBFVJWHF4YSYBJBPIWUP76LLSW47AC6JUVPO4Q3QDMYBGRUXWNHUID73T4L54HUHPYEJESTNKP24XHXYUQVVY"
                    }
                }
            }
        }
        attack_request = {
            "session": {
                "sessionId": "amzn1.echo-api.session.c398c68a-7578-41d2-91f2-fe12b670f679",
                "user": {
                    "userId": "amzn1.ask.account.AEEJPMHKHF2DINXCST2H3GAKEG5H5V2JCO6WH5PULVUYQ7PHPDNC2I6VORS4FG2YJ3TJDUOCCFWZYVBDIRHAINSQG2MRVZKJMA7GY3SKGPUHR6ZRQAFGXD5FMOKBFVJWHF4YSYBJBPIWUP76LLSW47AC6JUVPO4Q3QDMYBGRUXWNHUID73T4L54HUHPYEJESTNKP24XHXYUQVVY"
                },
                "new": False,
                "application": {
                    "applicationId": "amzn1.ask.skill.ceccea0b-f170-4541-b01c-a054a9a5676b"
                }
            },
            "version": "1.0",
            "request": {
                "intent": {
                    "slots": {
                        "item": {
                            "value": "spoon",
                            "name": "item"
                        }
                    },
                    "name": "attackNoMonsterIntent"
                },
                "locale": "en-US",
                "requestId": "amzn1.echo-api.request.cda5a835-a17e-4803-83ef-e3d64bcbd567",
                "type": "IntentRequest",
                "timestamp": "2016-09-25T01:10:47Z"
            },
            "context": {
                "AudioPlayer": {
                    "playerActivity": "IDLE"
                },
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.ceccea0b-f170-4541-b01c-a054a9a5676b"
                    },
                    "device": {
                        "supportedInterfaces": {
                            "AudioPlayer": {}
                        }
                    },
                    "user": {
                        "userId": "amzn1.ask.account.AEEJPMHKHF2DINXCST2H3GAKEG5H5V2JCO6WH5PULVUYQ7PHPDNC2I6VORS4FG2YJ3TJDUOCCFWZYVBDIRHAINSQG2MRVZKJMA7GY3SKGPUHR6ZRQAFGXD5FMOKBFVJWHF4YSYBJBPIWUP76LLSW47AC6JUVPO4Q3QDMYBGRUXWNHUID73T4L54HUHPYEJESTNKP24XHXYUQVVY"
                    }
                }
            }
        }

        response = requests.post(self.URL, json=take_request)
        print('take: %s' % str(response.json()))
        self.assertTrue('outputSpeech' in response.json()['response'])
        self.assertTrue('card' in response.json()['response'])

        response = requests.post(self.URL, json=attack_request)

        print('attack: %s' % str(response.json()))
        self.assertTrue('outputSpeech' in response.json()['response'])
        self.assertTrue('card' in response.json()['response'])
