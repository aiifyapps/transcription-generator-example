#!/usr/bin/env python

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
MODEL = 'whisper-1'

client = OpenAI(
    api_key=OPENAI_SECRET_KEY
)       

audio_file = open("source/output.mp3", "rb")
transcript = client.audio.transcriptions.create(model=MODEL, file=audio_file, response_format='srt', language='sr') 

with open("subtitles.srt", "w") as text_file:
    text_file.write(transcript)
