# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/59/problem/A

x = input()
capital = 0
small = 0
for i in x : 
    if ord(i)>=65 and ord(i)<=90 : 
        capital+=1
    else :
        small+=1

if capital > small : 
    print(x.upper())
else :
    print(x.lower())