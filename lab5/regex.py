import re

pattern = re.compile(r'ab*')

def match_string(s):
    return bool(pattern.match(s))

print(match_string("acccb"))
print(match_string("aaacbaaaaaaaa"))    


import re

pattern = re.compile(r'ab{2,3}')

def match_string(s):
    return bool(pattern.match(s))


print(match_string("ab"))    
print(match_string("abb"))    



import re

pattern = re.compile(r'[a-z]+_[a-z]+')

def find_sequences(s):
    return pattern.findall(s)


print(find_sequences())  


import re

pattern = re.compile(r'[A-Z][a-z]+')

def find_sequences(s):
    return pattern.findall(s)


print(find_sequences()) 




import re

pattern = re.compile(r'a.*b$')

def match_string(s):
    return bool(pattern.match(s))


print(match_string("acb"))   
print(match_string("ahdhdde"))    








import re

def replace_chars(s):
    return re.sub(r'[ ,.]', ':', s)


print(replace_chars("a, b. c d e")) 




def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))


print(snake_to_camel("hello_world")) 
print(snake_to_camel("came to"))  



import re

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)

print(split_at_uppercase("HelloWorld"))
print(split_at_uppercase("came to")) 


import re

def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)


print(insert_spaces("HelloWorld"))  
print(insert_spaces("came to")) 

import re

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


print(camel_to_snake("HelloWorld")) 
print(camel_to_snake("came to")) 






















