## language_corrector
Contains methods used for language correction. It's in python. You need to have done:

`pip install --upgrade language-check`

in command line to install the language check library that supports this library.

# How to use:
There's really only one way to use it. See as follows:

```python
import language_corrector.grammar_checker
text = "Text to check grammar for."
print(language_corrector.grammar_checker.basic_grammar_check(text))
```

# How to install:
In command line, navigate to inside the language correction folder, then run:

`python develop setup.py`
