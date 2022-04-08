from cgi import test
import os
from gtts import gTTS
mytext = "hello i am god's man"
language = "en"  # speech language
output = gTTS(text=mytext, lang=language, slow=False)
# default slow == true

output.save("output.mp3")

os.system("start output.mp3")
# to start that mp3 file.
