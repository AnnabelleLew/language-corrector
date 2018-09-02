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

def long_suggestion_grammar_check(text):
    """
    This method returns a longer list of suggestions, which can then be looped
    through if desired.

    Parameters
    ----------
        text : str
            The text that is inputted. Should be unformatted.

    Returns
    -------
        list of str
            Returns a list of suggestions.
    """
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    for i, match in enumerate(matches):
        fromy = match.fromy + 1
        fromx = match.fromx + 1
        ruleId = match.ruleId
        replacement = match.replacements[0]
        matches[i] = "Line {}, column {}, Rule ID: {}[{}]\nMessage: Did you mean '{}'?\nSuggestion: {}".format(fromy, fromx, ruleId, i, replacement, replacement)
    return matches

def num_of_errors(text):
    """
    This method returns the number of errors found in the text as an integer.

    Parameters
    ----------
        text : str
            The text that is inputted. Should be unformatted.

    Returns
    -------
        int
            Returns the number of errors in the text.
    """
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    errors = len(matches)
    return errors

def recommended_correction(text):
    """
    This method returns a recommended correction based off of the given text.

    Parameters
    ----------
        text : str
            The text that is inputted. Should be unformatted.

    Returns
    -------
        str
            Returns the recommended correction for the text.
    """
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    correction = language_check.correct(text, matches)
    return correction
