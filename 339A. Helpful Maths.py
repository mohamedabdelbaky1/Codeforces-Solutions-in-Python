# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/339/problem/A


x = input()
only_numbers = []
for i in x : 
    if i!="+" : 
        only_numbers.append(int(i))

only_numbers.sort()
for i in range(len(only_numbers)-1) : 
    print(f"{only_numbers[i]}+",end="")
print(only_numbers[-1])