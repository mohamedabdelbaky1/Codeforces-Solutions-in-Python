# Author : Mohamed Abdelbaky 
# Problem Link : https://codeforces.com/contest/9/problem/A

import math
y , w = map(int , input().split())
numerator = 6 - max(y,w)+1 
denominator = 6 

GCD = math.gcd(numerator,denominator)
numerator = numerator//GCD
denominator = denominator//GCD
print(f"{numerator}/{denominator}")

