import re

with open('Day1Input.txt') as f:
    lines = f.readlines()
    
valuesTable = []
allTotal = 0
for i in range(0,1000):#change back to 1000
    l=lines[i]
    #r=re.findall(r'\d', l)
    r=re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',l)
    #(r'(\d|one|ne|two|wo|three|hree|four|five|six|seven|eight|ight|nine|ine)', l)
    print(l,r)
    last=len(r)-1
    
    print(i,' ', r[0], r[last])
    
    if r[0]=='one':
        r[0]='1'
    if r[last]=='one':
        r[last]='1'
    if r[0]=='two':
        r[0]='2'
    if r[last]=='two':
        r[last]='2'
    if r[0]=='three':
        r[0]='3'
    if r[last]=='three':
        r[last]='3'
    if r[0]=='four':
        r[0]='4'
    if r[last]=='four':
        r[last]='4'
    if r[0]=='five':
        r[0]='5'
    if r[last]=='five':
        r[last]='5'
    if r[0]=='six':
        r[0]='6'
    if r[last]=='six':
        r[last]='6'
    if r[0]=='seven':
        r[0]='7'
    if r[last]=='seven':
        r[last]='7'
    if r[0]=='eight':
        r[0]='8'
    if r[last]=='eight':
        r[last]='8'
    if r[0]=='nine':
        r[0]='9'
    if r[last]=='nine':
        r[last]='9'

    print(r[0], r[last])

    lineTotal = int((r[0]) + (r[last]))
    print(lineTotal)
    allTotal += lineTotal
    print(allTotal)
    
    
    