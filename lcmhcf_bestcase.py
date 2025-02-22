def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> list[int]:
        g=gcd(a,b)
        l=(a*b)//g
        return [l,g]
#this takes O(log(min(a,b))) time complexity, which is optimized