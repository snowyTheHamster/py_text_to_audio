# Install required Apps and Modules
# apt install mpg123
# pip install gTTS
# pip install beautifulsoup4
# pip install markdown


from gtts import gTTS
import os
import markdown
from bs4 import BeautifulSoup


# text file path
textfile = "sample.md" # Select the script file for conversion
textdir = "scripts_original"
fullpath = os.path.join(textdir, textfile)

# audio file path
audiofile = f'{textfile.split(".")[0]}.mp3'
audiodir = "output_audio"
audiofull = os.path.join(audiodir, audiofile)


# convert markdown to text
html = markdown.markdown(open(fullpath).read())
script = "".join(BeautifulSoup(html, features="html.parser").findAll(text=True))
print(script)


# initialize tts and save file
tts = gTTS(script, lang="en-us")
tts.save(audiofull)
# os.system("mpg123 " + audiofull) #toggle on/off to play audio automatically