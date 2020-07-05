import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

https://www.google.com
http://coreyms.com
https://youtube.com
'''

#email address
#pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
     
    
    
'''   
with open('textRegex.txt','r', encoding='utf-8') as f:
    contents = f.read()
    
    matches = pattern.finditer(contents)
    '''
#    for match in matches:
#        print(match)
    
#print(matches)