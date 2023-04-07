
import math

key = list(map(int, input().split()))
signal = list(map(float, input().split())) 

coords = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

c = 0

j=0
for i in range(len(key)):
    inv = (key[i] + 1)**2
    coords[j][c%2] = round(signal[i]*inv)
    c+=1
    if(c%2==0 and c!=0):
        j+=1

for i in range(len(key)):
    inv = (key[i] + 2)**1.5
    coords[j][c%2] = round(signal[i+4]*inv)
    c+=1
    if(c%2==0 and c!=0):
        j+=1

for i in range(len(key)):
    inv = (key[i] + 3)**3
    coords[j][c%2] = round(signal[i+8]*inv)
    c+=1
    if(c%2==0 and c!=0):
        j+=1

print(coords)