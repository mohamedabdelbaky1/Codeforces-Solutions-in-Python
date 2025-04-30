# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/265/problem/A

x = input()   # RRRBGBRBBB
y = input()   # BBBRR

start = 1 
for i in range(len(y)) : 
    if y[i]==x[start-1] : 
        start+=1
    
print(start)
