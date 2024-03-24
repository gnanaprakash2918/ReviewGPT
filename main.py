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


product_url = input('Enter The URL of the Amazon Product : ')

while True:
  user_query = input('Enter your query about the product : ')
  if(user_query == 'end'):
    break
  
  response = model.generate_content(f'Goto this product link ${product_url} and read about the product details and answer this query ${user_query}')
  
  # Reinitialize the Model
  model = genai.GenerativeModel('gemini-pro')
  print(md_to_text(response.text))

