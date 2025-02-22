def armstrong(num):
    n = len(str(num))
    arm = 0
    x = num  # Copy of num
    while x > 0:
        digit = x % 10  # Extract last digit
        arm += digit ** n
        x //= 10  # Remove last digit
    return arm == num
#time complexity is same as the best case, i.e. O(n log n)
#but this has more complex calculations than best case