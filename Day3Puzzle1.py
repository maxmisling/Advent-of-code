import re
import numpy as np
lines = list(open('Day3TestInput.txt', 'r'))

# with open(file) as txt:
#     line = [elem.strip().split('\t') for elem in tsv]

l=[]
for i in range(0,10):
    row=lines[i]
    r=re.findall(r'(\d|.|#|$|/*)', row)
    #print(row, type(row),r)
    if i < 9:
        r=r[:-2]
    else:
        r=r[:-1]
        
    l.append(r)

#l = l[:-1]

vals = np.asarray(l)
#r=re.findall(r'(\d+|.|*|#|$)', vals)

#for i in range(0,10):
    #valsRow=vals[i]
    #r=re.findall(r'(\d+|.|*|#|$)', valsRow)
    #print(r)
for i in range(0,10):
    for j in range(0,10):
        val=vals[i][j]
        if val == '*' or val == '#' or val == '$' or val =='+':   
            print('equals ', val,i,j)
            if i ==0:
                print(vals[i][j-1],vals[i][j],vals[i][j+1],vals[i+1][j-1],vals[i+1][j],vals[i+1][j+1])
            if i ==9:
                print(vals[i-1][j-1],vals[i-1][j],vals[i][j-1],vals[i][j],vals[i][j+1],vals[i+1][j-1])
            if j ==0:
                print(vals[i-1][j],vals[i-1][j+1],vals[i][j],vals[i][j+1],vals[i+1][j],vals[i+1][j+1])
    
            if j ==9:
                print(vals[i-1][j-1],vals[i-1][j],vals[i][j-1],vals[i][j],vals[i+1][j-1],vals[i+1][j])
                           
            else:
                print(vals[i-1][j-1],vals[i-1][j],vals[i-1][j+1],vals[i][j-1],vals[i][j],vals[i][j+1],vals[i+1][j-1],vals[i+1][j],vals[i+1][j+1])
