# Author : Mohamed Abdelbaky
# Problem Link : https://codeforces.com/problemset/problem/69/A

n = int(input())
matrix = []
for i in range(n) : 
    row = list(map(int,input().split()))
    matrix.append(row)

sumX = 0
sumY = 0
sumZ = 0
for i in range(n) :
    sumX+= matrix[i][0]
    sumY+= matrix[i][1]
    sumZ+=matrix[i][2]

if sumX ==0 and sumY ==0 and sumZ ==0 : 
    print("YES")
else : 
    print("NO")