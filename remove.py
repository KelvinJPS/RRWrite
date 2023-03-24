import nltk


def remove_punctuation_marks(text: str) -> str:
    punctuation_marks = ['.', '?', ',', ';']
    for mark in punctuation_marks:
        text = text.replace(mark, "")
    return text


def remove_world_class(text: str, TAG: str) -> str:
  tokens = nltk.word_tokenize(text)
  tagged = nltk.pos_tag(tokens, tagset='universal')
  for world, tag in tagged:
    if tag == TAG:
        text = text.replace(world, "")
  return text
  

def remove_adjetives(text: str) -> str:
    return remove_world_class(text,'ADJ')

def remove_adverbs(text: str) -> str:
    return remove_world_class(text, 'ADV')

def remove_verbs(text: str) -> str:
    return remove_world_class(text, 'VERB')


 
