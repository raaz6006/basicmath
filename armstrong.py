def armstrong(num):
    n=len(str(num))
    arm=0
    l=list(str(num))
    for i in range(n):
        arm+=(int(l[i]))**n
    return arm==num
#time complexity is O(n log n)
