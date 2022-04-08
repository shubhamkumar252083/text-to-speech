from cgi import test
import os
from gtts import gTTS
# mytext = "hello i am god's man"
# name of text file to convert. (in read mode)
file_handler = open("test.txt", "r")
# removing line endings from text file.
mytext = file_handler.read().replace("\n", " ")


language = "en"  # speech language
output = gTTS(text=mytext, lang=language, slow=False)
# default slow == true

output.save("output2.mp3")
file_handler.close()

os.system("start output2.mp3")
# to start that mp3 file.


'''
(class) gTTS
gTTS -- Google Text-to-Speech.

An interface to Google Translate's Text-to-Speech API.

Args:
    text (string): The text to be read.
    tld (string): Top-level domain for the Google Translate host,
        i.e https://translate.google.<tld>. Different Google domains can produce different localized 'accents' for a given language. This is also useful when google.com might be blocked within a network but a local or different Google host (e.g. google.cn) is not. Default is com.
    lang (string, optional): The language (IETF language tag) to
        read the text in. Default is en.
    slow (bool, optional): Reads text more slowly. Defaults to False.
    lang_check (bool, optional): Strictly enforce an existing lang,
        to catch a language error early. If set to True, a ValueError is raised if lang doesn't exist. Setting lang_check to False skips Web requests (to validate language) and therefore speeds up instanciation. Default is True.
    pre_processor_funcs (list): A list of zero or more functions that are
        called to transform (pre-process) text before tokenizing. Those functions must take a string and return a string. Defaults to:

[
    pre_processors.tone_marks,
    pre_processors.end_of_line,
    pre_processors.abbreviations,
    pre_processors.word_sub
]
    tokenizer_func (callable): A function that takes in a string and
        returns a list of string (tokens). Defaults to:

Tokenizer([
    tokenizer_cases.tone_marks,
    tokenizer_cases.period_comma,
    tokenizer_cases.colon,
    tokenizer_cases.other_punctuation
]).run
See Also:
    Pre-processing and tokenizing <tokenizer>

Raises:
    AssertionError: When text is None or empty; when there's nothing
        left to speak after pre-precessing, tokenizing and cleaning.
    ValueError: When lang_check is True and lang is not supported.
    RuntimeError: When lang_check is True but there's an error loading
        the languages dictionary.

'''
