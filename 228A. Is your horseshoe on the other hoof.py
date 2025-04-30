# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/228/problem/A

horseshoes = list(map(int , input().split()))
unique_horseshoes = list(set(horseshoes))
print(4 - len(unique_horseshoes))