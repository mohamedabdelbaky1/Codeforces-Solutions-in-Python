# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/443/problem/A

x = input()
if len(x) == 2 :    # {}
    print(0)
elif len(x)==3 :    # {a}
    print(1)
else :
    Unique_x = set(x)
    print(len(Unique_x)-4)