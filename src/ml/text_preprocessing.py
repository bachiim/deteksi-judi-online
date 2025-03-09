import string
import emoji
import re

def to_lower(text: str):
  """Mengubah teks menjadi lowercase"""
  return text.lower()

def remove_emoji(text: str):
  """Menghapus emoji dari teks"""
  text = emoji.demojize(text)
  return re.sub(r":\S+:", "", text)

def remove_punctuation(text: str):
  """Menghapus tanda baca dari teks"""
  return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text: str):
  """Menghapus stopwords dari teks"""
  with open('../data/stopwords-id.txt', 'r', encoding='utf-8') as file:
    stopwords = file.read().splitlines()

  words = text.split()
  filtered_words = [word for word in words if word not in stopwords]
  return ' '.join(filtered_words)