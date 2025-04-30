# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/732/problem/A

k , r = map(int , input().split())
for i in range(1,10) : 
    if (k*i) % 10 == 0 or (k*i) % 10 == r :       # we do not need to loop over all numbers but we will loop just from 1 t0 9 
        print(i)                                  # because if no number between 1 and 9 is true this means that the minimum shovels = 10 
        break 
else :
    print(10)