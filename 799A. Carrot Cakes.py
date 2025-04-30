# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/799/problem/A


n ,t , k , d = map(int , input().split())
if (n-1) // k * t > d : 
    print("YES")
else : 
    print("NO")
