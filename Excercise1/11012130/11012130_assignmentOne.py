import re

import multiprocessing as mp 
from contextlib import contextmanager


@contextmanager
def bible_function(path, mode):
    y = open(path, mode)
    yield y 
    y.close()
    
class Bible_Count(mp.Process):
    def run(self):
        with bible_function(r"C:\Users\yasha\OneDrive\Desktop\Big Data Programming2\Code\Excercise1\bible.txt", 'r') as c:
            contents = c.read()
            count_matches = re.findall('earth', contents, re.IGNORECASE)
            print(len(count_matches))
        
        
processess = []
if __name__ == "__main__":
    for i in range(2):
        startProcess = Bible_Count() 
        processess.append(startProcess)
        startProcess.start()

for j in processess:
    j.join()