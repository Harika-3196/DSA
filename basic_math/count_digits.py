def count_digits_bruteforce(n):
    count=0
    while(n>0):
        count+=1
        n=n//10
        # print(n)
    return count

count=count_digits_bruteforce(n=10045)
print("count using bruteforce",count)


# brute force
# time complexity
# in the while loop we divide n by 10 which takes log10N . we also perform constant operations like division and inrement counter so it is O(1og10N+1)

#Space complexity
#o(1) only a constant amount of memory needed for counter regardless of number od digits

import math
def count_digits_optimal(n):
    digits =int((math.log10(n)+1)) # 1 because n itself might be power of 10
    return digits

count=count_digits_optimal(n=10045)
print("count using optimal",count)

#optimal
#time complexity
# o(1) is simple arithmetic operations in constant time computed on integers
#space complexity : o(1) constant amount of additional memory for the count regardless of number of input number
