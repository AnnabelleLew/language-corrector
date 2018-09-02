# language_corrector
Contains methods used for language correction. It's in python. You need to have done:

`pip install --upgrade language-check`

in command line to install the language check library that supports this library.

## How to use:
Here's the easiest way to use it. See as follows:

```python
import language_corrector.grammar_checker
text = "Text to check grammar for."
print(language_corrector.grammar_checker.basic_grammar_check(text))
```

## Methods available:
- `basic_grammar_check()`: returns feedback based on the grammar check
- `long_suggestion_grammar_check()`: returns a list of each suggestion
- `num_of_errors()`: returns the number of errors
- `recommended_correction()`: returns a recommended correction

## How to install:
Download as a .zip file and unzip. Then, in command line, navigate to inside the language correction folder, then run:

`python develop setup.py`
