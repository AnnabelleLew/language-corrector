import language_check

def basic_grammar_check(text):
    """
    This method does a basic grammar check on plaintext, and returns the number
    of errors and a recommended correction.

    Parameters
    ----------
        text : str
            The text that is inputted. Should be unformatted.

    Returns
    -------
        str
            Returns text in the following format:
            "There are {} errors.
            Recommended correction: {}"
    """
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    feedback = "There are {} errors.".format(len(matches))
    correction = language_check.correct(text, matches)
    feedback += "\nRecommended correction: {}".format(correction)
    return feedback
