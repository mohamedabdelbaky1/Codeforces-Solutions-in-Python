# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/490/problem/A 


n = int(input())
children = list(map(int , input().split()))

list1 = []
list2 = []
list3 = []
for i in range(len(children)) : 
    if children[i]==1 : 
        list1.append((1,i+1))
    elif  children[i]==2 : 
        list2.append((2,i+1))
    else : 
        list3.append((3,i+1))

num_of_teams = min(len(list1),len(list2),len(list3))
print(num_of_teams)
for i in range(num_of_teams) : 
    print(f"{list1[i][1]} {list2[i][1]} {list3[i][1]}")