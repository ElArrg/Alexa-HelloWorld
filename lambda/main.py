# -*- coding: utf-8 -*-
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

skill = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SKILL_NAME = "Hola Mundo"
HELP_MESSAGE = "Puedes pedirme decir hola mundo."


@skill.request_handler(can_handle_func = is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    speech_text = "Bienvenido a tu hola mundo en Alexa. " + HELP_MESSAGE

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(SKILL_NAME, speech_text)).set_should_end_session(
        False).response


@skill.request_handler(can_handle_func = is_intent_name("HelloWorldIntent"))
def hello_world_intent_handler(handler_input):
	speech_text = "Hola mundo Alexa Skills."

	return handler_input.response_builder.speak(speech_text).set_card(
		SimpleCard(SKILL_NAME, speech_text)).set_should_end_session(True).response


@skill.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    speech_text = HELP_MESSAGE

    return handler_input.response_builder.speak(speech_text).ask(
        speech_text).set_card(SimpleCard(SKILL_NAME, speech_text)).response


@skill.request_handler(
    can_handle_func=lambda handler_input:
        is_intent_name("AMAZON.CancelIntent")(handler_input) or
        is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
    speech_text = "Adiós"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(SKILL_NAME, speech_text)).response


@skill.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):

    return handler_input.response_builder.response


@skill.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    logger.error(exception, exc_info=True)

    speech = "<say-as interpret-as='interjection'>achís achís, no sé que pasó</say-as>"
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response


lambda_handler = skill.lambda_handler()