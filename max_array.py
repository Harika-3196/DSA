

a=[2,5,7,8,10,-1]
#1) question : find max of array
from typing import List
def max_array(a):
    a.sort()
    return a[-1]

print("using sort",max_array(a))

def max_array_using_recursion(a,n):
    max1 =a[0]
    for i in range(0,n):
        if max1<a[i]:
           max1=a[i]
    return max1

print("max array using recursion",max_array_using_recursion(a,len(a)))


