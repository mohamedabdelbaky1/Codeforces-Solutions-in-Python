# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/731/problem/A

x = input()
pointer = 97               
ans = 0
for i in x : 
    a = ord(i) - pointer
    if a<0 :
        a+=26
    b = pointer - ord(i)
    if b<0 : 
        b+=26
    if a<=b : 
        ans+=a
    else :
        ans+=b 
    pointer = ord(i)

print(ans)
