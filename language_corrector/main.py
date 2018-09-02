import language_corrector.grammar_checker as gc
from google.cloud import translate

def return_english(text):
    """
    This method returns a grammar check in English.

    Parameters
    ----------
        text : str
            The text that is inputted. Should be unformatted.

    Returns
    -------
        str
            In the format:
            "Text: {}
            Recommended Grammar English: {}"
    """
    # message = input from bot
    english_grammar = gc.recommended_correction(text)
    output = "Text: {}".format(text)
    #print('Confidence: {}'.format(result['confidence']))
    #print('Language: {}'.format(result['language']))
    output += "\nRecommended Grammar English: {}".format(english_grammar)
    return output

def return_translation(text, target='fr'):
    """
    This method returns a grammar check in a requested language.

    Parameters
    ----------
        text : str
            The text that is inputted. Should be unformatted.
        target : str
            The target language to translate into.

    Returns
    -------
        str
            In the format:
            "Text: {}
            Recommended Grammar: {}
            Recommended Grammar Translation: {}"
    """
    english_grammar = gc.recommended_correction(text)
    translated_grammar = translate.Client()
    translated_grammar = translated_grammar.translate(english_grammar, target_language=target)
    output = u"Text: {}".format(text)
    output += u"\nRecommended Grammar: {}".format(english_grammar)
    output += u"\nRecommended Grammar Translation: {}".format(translated_grammar['translatedText'])
    return output
