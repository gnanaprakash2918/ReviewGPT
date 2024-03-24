import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# To Read API KEY from .env
from decouple import Config, RepositoryEnv
env=Config(RepositoryEnv('.env'))

# Convert to md
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# https://aistudio.google.com/app/apikey
genai.configure(api_key=env.get('GOOGLE_API_KEY'))

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)