import re
# open the data file
#f = open('Day2Input.txt')
# read the file as a list

#lines = list(open('Day2Input.txt', 'r'))

#with open('Day2TestInput.txt') as f:
lines = list(open('Day2Input.txt', 'r'))

values = []
valuesInts = []
valuesColours = []
gameNumber = []
gameResults = []
for n in range(0,100):
    l=lines[n]
    r=re.findall(r'(\d+|;|red|blue|green)', l)
    rColours=re.findall(r'(red|blue|green)', l)
    rInts=re.findall(r'(\d+)', l)
    rInts=rInts[1:len(rInts)]
#(r'(\d|one|ne|two|wo|three|hree|four|five|six|seven|eight|ight|nine|ine)', l)
    values.append(r)
    valuesInts.append(rInts)
    valuesColours.append(rColours)

#for n in range(0,5):
    #gameNumber.append(values[n][0])

for n in range(0,100):
    gameResults.append(values[n][1:len(values)-1])
    gameNumberInt=int(values[n][0])
    gameNumber.append(gameNumberInt)
    
count=[]  
for n in range(0,100):
    row=valuesInts[n]
    rowColours=valuesColours[n]
    for i in range(0,len(row)):
        j = int(row[i])
        k = rowColours[i]
        
        if j > 12:
            print(n+1,j,', entry:',i+1,k) 
            if k == 'red':
                gameID=n+1
                print(k, gameID)
                count.append(gameID)
        
        if j > 13:
            print(n+1,j,', entry:',i+1,k) 
            if k == 'green':
                gameID=n+1
                print(k, gameID)
                count.append(gameID)
                
        if j > 14:
            print(n+1,j,', entry:',i+1,k) 
            if k == 'blue':
                gameID=n+1
                print(k, gameID)
                count.append(gameID)
    
print('count:',count)

#a=set(gameNumber)
countID=set(gameNumber)
imPossible=set(gameNumber) & set(count)
#print('Impossible:', imPossible)
Possible=countID.difference(imPossible)
print(Possible)
#print(set(a) & set(b))
possCount=0
for i in Possible: possCount+=i
print('Sum of Possible Game IDs: ', possCount)
#if a == b: print('y:',b)