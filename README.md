# Python Text to Audio

Convert text in a markdown file into an audio file.

## installation

install the required apps & modules

```
apt install mpg123
pip install gTTS
pip install beautifulsoup4
pip install markdown
```

or

```
pip install -r requirements.txt
```

## how to use

+ prepare a md file in the **scripts_original** folder.

+ update filename in **run.py**.

to run:

```
python run.py
```

The audio file will be saved in the **output_audio** folder.

The system will also play the audio file.