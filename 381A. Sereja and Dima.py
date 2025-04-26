# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/381/problem/A

n = int(input())
cards = list(map(int,input().split()))
left = 0
right = n-1

sereja_points = 0
dima_points = 0
for i in range(n) :
    if cards[left]<cards[right] and i%2==0 :               
        sereja_points+=cards[right]
        right-=1
    elif cards[left]>=cards[right] and i%2==0 :
        sereja_points+=cards[left]
        left+=1
    elif cards[left]<cards[right] and i%2!=0 : 
        dima_points+= cards[right]
        right-=1
    elif cards[left]>=cards[right] and i%2!=0 :
        dima_points+=cards[left]
        left+=1

print(sereja_points , dima_points)
