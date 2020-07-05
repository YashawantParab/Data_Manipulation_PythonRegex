import re

import multiprocessing
from contextlib import contextmanager
'''
def earth():
    print ('earth')
    return

if __name__ == '__main__':
    jobs = []
    for i in range(2):
        p = multiprocessing.Process(target=earth)
        jobs.append(p)
        p.start()

pattern = re.finditer(r'earth', re.I)

with open('bible.txt','r', encoding='utf-8') as f:
    contents = f.read()
    
    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)
 
#print(len(pattern))
'''

class bible():
    def __init__(self, word, word_count):
        self.word = word
        self.word_count = word_count
        
    def __enter__(self):
        self.file = open(self.word, self.word_count)
        return self.file
        
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        




pattern = re.compile(r'earth', re.I)


with bible('bible.txt','r') as y:
    contents = y.read()
    
    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)
        
@contextmanager
def bible_function(word, word_count):
    y = open(word, word_count)
    yield y 
    y.close()
    
with bible_function('bible.txt', value) as f:
    f.count(match)
    
    print(match.count('earth'))
   
