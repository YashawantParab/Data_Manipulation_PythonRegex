import re

import multiprocessing as mp 
from contextlib import contextmanager


@contextmanager
def bible_function(name, mode):
    y = open(name, mode)
    yield y 
    y.close()
    
class bible_Count(mp.Process):
    def run(self):
        with bible_function('bible.txt', 'r' ) as c:
            contents = c.read()
            matches = re.findall('earth', contents, re.I)
            print(len(matches))
        
        
processess = []
for i in range(2):
    startProcess = bible_Count() 
    processess.append(startProcess)
    startProcess.start()

for j in processess:
    j.join()