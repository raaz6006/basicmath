def gcd(a, b):
    hcf = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf

class Solution:
    def lcmAndGcd(self, a: int, b: int):
        g = gcd(a, b)
        l = (a * b) // g
        return [l, g]
#time complexity for above is O(min(a,b))