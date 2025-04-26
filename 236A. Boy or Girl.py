# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/236/problem/A


x = input()
freq = [0] * 27   # this is an initialization for 27 elements in list where all elements = 0
for i in x : 
    if freq[ord(i)-97] == 0 :
       freq[ord(i)-97]+=1     # ord() is used to convert from character to ascii code and 97 is ascii code for 'a'

counter=0
for i in freq : 
    counter+=i

if counter%2==0 : 
    print("CHAT WITH HER!")
else : 
    print("IGNORE HIM!")