# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/problemset/problem/791/A


x,y = map(int,input().split())
c=0
while x<=y : 
    x*=3
    y*=2
    c+=1
print(c)