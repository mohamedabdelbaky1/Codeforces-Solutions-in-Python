# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/427/problem/A

n = int(input())
myList = list(map(int,input().split()))
police_officers = 0
crimes=0
for i in range(n) : 
    if myList[i]>0 :
        police_officers+=myList[i]
    else :
        if police_officers==0 :
            crimes+=1
        else :
            police_officers+=myList[i]

print(crimes)