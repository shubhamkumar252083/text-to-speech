from cgi import test
import os
from gtts import gTTS


def fn(*args):
    file_handler = open(args[0], "r")
    mytext = file_handler.read().replace("\n", " ")
    language = args[1]
    # tld='com.au',
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save(args[2]+".mp3")
    file_handler.close()
    os.system("start"+args[2]+".mp3")
