# Author : Mohamed Abdelbaky
# Problem Link : https://codeforces.com/problemset/problem/131/A

x = input()
for i in range(1,len(x)) : 
    if x[i] >= 'a' : 
        print(x)
        break
else : 
    if x[0] >= 'a' : 
        print(x.capitalize())
    else : 
        print(x.lower())