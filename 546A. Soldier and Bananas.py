# Author : Mohamed Abdelbaky
# Problem Link : https://codeforces.com/problemset/problem/546/A

k,n,w = list(map(int , input().split()))
borrow = (w * (w+1) // 2 ) *k - n 
if borrow > 0 : 
    print(borrow)
else : 
    print(0)