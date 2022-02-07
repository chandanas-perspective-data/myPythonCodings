import re

def parse_code(txt):
  first, second, _id = re.split('0+', txt)
  return {'first_name': first, 'last_name': second, 'id': _id}


print (parse_code("John000Doe000123"))