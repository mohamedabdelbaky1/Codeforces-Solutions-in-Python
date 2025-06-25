# Author : Mohamed Abdelbaky
# Problem Link : https://codeforces.com/problemset/problem/617/A

n = int(input())
if n%5==0 : 
    print(int(n/5))
else : 
    print(n//5+1)