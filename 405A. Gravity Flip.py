# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/problemset/problem/405/A

n = int(input())
myList = list(map(int,input().split()))

myList.sort()
for i in myList : 
    print(i , end = " ")