# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/problemset/problem/263/A


matrix = []
for i in range(5) : 
    col = list(map(int,input().split()))
    matrix.append(col)


for i in range(5) : 
    for j in range(5) :
        if matrix[i][j]==1 :
            ans = abs(2-i) + abs(2-j)
            break

print(ans)    
