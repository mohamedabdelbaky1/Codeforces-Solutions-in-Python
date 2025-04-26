# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/problemset/problem/677/A


n , h = map(int,input().split())
a = list(map(int,input().split()))
c=0
for i in a : 
    if i>h : 
        c+=2
    else :
        c+=1

print(c)