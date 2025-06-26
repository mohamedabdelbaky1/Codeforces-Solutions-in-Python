# Author : Mohamed Abdelbaky
# Problem Link : https://codeforces.com/problemset/problem/25/A

n = int(input())
arr = list(map(int  , input().split()))
even = []
odd = []
E = 0 
O = 0
for i in range(n) : 
    if arr[i]%2==0 : 
        even.append(arr[i])
        even.append(i)
        E+=1
    else :
        odd.append(arr[i])
        odd.append(i)
        O+=1
if E==1 : 
    print(even[1]+1)
else : 
    print(odd[1]+1)