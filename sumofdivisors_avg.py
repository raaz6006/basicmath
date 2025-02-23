class Solution:
    def sumOfDivisors(self, n):
        total=0
        for i in range(1,n+1):
            sum_divisors=0
            for j in range(1,i+1):
                if i%j==0:
                    sum_divisors+=j
            total+=sum_divisors
        return total
#time complexity is O(n^2)