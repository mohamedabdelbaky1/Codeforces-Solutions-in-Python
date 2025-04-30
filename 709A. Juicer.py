# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/709/problem/A

# take the input
n,b,d = map(int , input().split())
oranges = list(map(int , input().split()))

# Implementation
size = 0 
res = 0
for i in oranges : 
    if i<=b : 
        size+=i
        if size > d : 
            res+=1 
            size = 0

# output
print(res)
