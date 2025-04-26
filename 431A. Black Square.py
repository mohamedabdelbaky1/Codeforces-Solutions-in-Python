# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/431/problem/A

myList = list(map(int,input().split()))
x = input()

dict = {}
ans = 0
for i in range(len(myList)) : 
    dict[i+1] = myList[i]

for i in x : 
    ans+= dict[int(i)]
print(ans)