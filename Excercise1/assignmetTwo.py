a= 'yes'
b= 'no'
matrix = [['no' if i==j else 'yes' for j in range(5)] if i !=4 else ['no' for i in range(5)] for i in range(5)]

"""
for j in range(5):
    for i in range(5):
        if j==i:
            matrix[j][i] = b
        elif j==4:
            matrix[j][i] = b  """
            
print(matrix) 

