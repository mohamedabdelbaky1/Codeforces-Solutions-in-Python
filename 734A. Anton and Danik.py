# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/problemset/problem/734/A



# First Solution

n = int(input())
x = input()
if x.count("A") > x.count("D") : 
    print("Anton")
elif x.count("A") < x.count("D") : 
    print("Danik")
else : 
    print("Friendship")

#<=============================================================================================================================================>

# Second solution : 

n = int(input())
x = input()
A=0
D=0
for i in x : 
    if i=='A' : 
        A+=1
    elif i=='D' : 
        D+=1

if A>D : 
    print("Anton")
elif A<D :
    print("Danik")
else : 
    print("Friendship")

#<===============================================================================================================================================>