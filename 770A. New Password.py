# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/770/problem/A

start = 97  # 'a' in ascii code 
n , k = map(int , input().split())
password = []
for i in range(n) : 
    password.append(chr(start))
    start+=1
    if start==97+k : 
        start = 97

NewPassword = "".join(password)
print(NewPassword)