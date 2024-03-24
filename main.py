import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# To Read API KEY from .env
from decouple import Config, RepositoryEnv
env=Config(RepositoryEnv('.env'))

# To Convert MD to Str
import markdown
from bs4 import BeautifulSoup

def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

# Convert to md
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# https://aistudio.google.com/app/apikey
genai.configure(api_key=env.get('GOOGLE_API_KEY'))

# Choose Model
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Do you Know Power rangers ?")

# Call to_markdown if needed
md = response.text
print(md_to_text(md))