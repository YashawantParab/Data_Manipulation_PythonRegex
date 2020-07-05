from pyparsing import line

"""def stringList(j):  
    
    # initialize an empty string 
    empty_string = ""  
    
    # traverse in the string   
    for element in j:  
        empty_string += element   
        #if ele == ',' or ele == '!':
             
    
    # return string
    return empty_string  """

#special_chars = [';', ':', '!', "*", ","] 
  
# initializing test string  
mainString = "hello, want to remove : this"
  
# printing original string  
  
# using filter() to  
# remove bad_chars  
"""lambda_results = []
test_string = list(lambda i: i not in special_chars, test_string) 
"""
#lambda_results.append(test_string)
#print(test_string)
#print(stringList(test_string))




def filterString(specialChar):
    return lambda line:list(map(lambda specialChar: line.replace(specialChar,""),specialChar))
#print(filterString(specialChar))
#print ("mainString : " + filterString) 

listSpecialCharacters = filterString([',',':'])
print(listSpecialCharacters(mainString))


'''
def compose1(f, g):
    return lambda x: f(g(x))
	
f = compose1(lambda x: x * x,
	        lambda y: y + 1)
result = f(12)
print(result)'''