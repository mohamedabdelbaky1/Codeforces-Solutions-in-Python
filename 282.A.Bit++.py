# Author : Mohamed Abdelbaky
# Problem Link : https://codeforces.com/problemset/problem/282/A

n = int(input())
ans = 0
while n : 
    x = input()
    if x == "X++" or x == "++X" : 
        ans+=1
    else : 
        ans-=1
    n-=1
print(ans)

