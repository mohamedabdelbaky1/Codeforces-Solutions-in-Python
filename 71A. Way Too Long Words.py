# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/71/problem/A


test_case = int(input())
for i in range(test_case) : 
    x = input()
    if len(x)>10 : 
        print(f"{x[0]}{len(x)-2}{x[-1]}")
    else: 
        print(x)


