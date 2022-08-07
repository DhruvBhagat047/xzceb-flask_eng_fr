""" Program to translate using Watson API """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    """ English to French """
    translation = language_translator.translate(text=englishtext,model_id='en-fr').get_result()
    french_output = translation['translations'][0]['translation']
    return french_output

def french_to_english(frenchtext):
    """ French to English """
    translation = language_translator.translate(text=frenchtext,model_id='fr-en').get_result()
    english_output = translation['translations'][0]['translation']
    return english_output
