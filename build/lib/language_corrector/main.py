import language_corrector.grammar_checker as gc
from google.cloud import translate

def return_english(text):
    # message = input from bot
    english_grammar = gc.recommended_correction(text)
    output = "Text: {}".format(text)
    #print('Confidence: {}'.format(result['confidence']))
    #print('Language: {}'.format(result['language']))
    output += "\nRecommended Grammar English: {}".format(english_grammar)
    return output

def return_translation(text, target='fr'):
    english_grammar = gc.recommended_correction(text)
    translated_grammar = translate.Client()
    translated_grammar = translated_grammar.translate(english_grammar, target_language=target)
    output = u"Text: {}".format(text)
    output += u"\nRecommended Grammar: {}".format(translated_grammar['translatedText'])
    return output
