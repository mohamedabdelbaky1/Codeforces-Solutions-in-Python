# Author : Mohamed Abdelbaky
# Problem Link : https://codeforces.com/problemset/problem/118/A

x = input()
y = []
for i in x : 
    if i=='a' or i=='A' or i=='e' or i== 'E' or i=='i' or i=='I' or i=='o' or i=='O' or i== 'u' or i=='U' or i=='y' or i=='Y' : 
        continue 
    else : 
        y.append(".")
        y.append(i.lower())
print("".join(y))