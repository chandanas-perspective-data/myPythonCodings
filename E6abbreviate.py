import re
def abbreviate(words):
    return "".join(word[0].upper() for word in re.sub(r'[_-]',' ', words).split())


print (abbreviate("National Geography"))