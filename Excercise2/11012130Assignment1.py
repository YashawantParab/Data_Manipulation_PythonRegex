
class Range:
    def __init__(self, start, stop):
        self.value = start
        self.end = stop
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
       # else:
            #pass
        
        #result = self.value
        self.value += 29
        return self.value

iterate = Range(0,100)
#next(iterate)
for something in iterate:
    print(something)
