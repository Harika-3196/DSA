from typing import List
a=[5,2,3,4,10,-1]


def second_smallest_without_sort(a):
   smallest_min =float('inf')
   second_min=float('inf')
   for i in range(len(a)):
       if (a[i]< smallest_min) :
           second_min = smallest_min
           smallest_min=a[i]
       elif (a[i]<second_min) & (a[i]!=smallest_min):
           second_min=a[i]
   return second_min,smallest_min

print("second smallest and smallest",second_smallest_without_sort(a))









