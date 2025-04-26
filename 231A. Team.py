# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/231/problem/A



# First Solution 

#Take the input 
row = int(input())
matrix = []
for i in range(row) :
    col = list(map(int,input().split()))
    matrix.append(col)

# Traverse the matrix 
Implemented_Problem = 0
for i in matrix : 
    if sum(i)>=2 :
        Implemented_Problem+=1

print(Implemented_Problem)

#<=============================================================================================================================================>

# Second Solution : 

# Take the input 
row = int(input())
matrix = []
for i in range(row) :
    col = list(map(int,input().split()))
    matrix.append(col)

# Traverse the matrix 
Implemented_Problem = 0
temp = 0
for i in matrix : 
    for j in i :
        temp+=j
    if temp>=2 :
        Implemented_Problem+=1
    temp = 0

print(Implemented_Problem)
#<==============================================================================================================================================>