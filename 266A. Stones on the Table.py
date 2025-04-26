# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/266/problem/A


n = int(input())
x= input()
ans = 0
for i in range(n-1) : 
    if x[i] == x[i+1] : 
        ans+=1

print(ans)