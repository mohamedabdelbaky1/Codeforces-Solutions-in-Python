# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/344/problem/A

num_of_magnets = int(input())

list_of_magnets = []

for i in range(num_of_magnets) : 
    magnet = input()
    list_of_magnets.append(magnet)

ans = 1
for i in range(num_of_magnets-1) : 
    if list_of_magnets[i] !=list_of_magnets[i+1] :
        ans+=1

print(ans)