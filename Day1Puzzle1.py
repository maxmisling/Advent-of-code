import re

with open('Day1Input.txt') as f:
    lines = f.readlines()
    
allTotal = 0
for i in range(0,1000):#change back to 1000
    l = lines[i]
    r=re.findall(r'\d', l)   
    last=len(r)-1
    lineTotal = int((r[0]) + (r[last]))
    allTotal += lineTotal
    
print(allTotal)
    
    
    