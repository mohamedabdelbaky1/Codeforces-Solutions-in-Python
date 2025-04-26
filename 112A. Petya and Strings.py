# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/problemset/problem/112/A

x = input()
y = input()

for i in range(len(x)) :       # Be careful : It is guaranteed that the strings are of the same length so len(x) = len(y)
    if x[i].lower()<y[i].lower() :
        print("-1")
        break 
    elif x[i].lower()>y[i].lower() : 
        print("1")
        break 
else :
    print("0")