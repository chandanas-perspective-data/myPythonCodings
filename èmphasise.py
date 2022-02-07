def emphasise(txt):
  return ' '.join(w[0].upper()+w[1:].lower() for w in txt.split())


print (emphasise("hello python"))