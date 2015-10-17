import numpy as np
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
	
       splitpoint = partition(alist,first,last)
 #      print alist
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   global count
   count += (last - first)
   l = []
   l.append(alist[first])
   l.append(alist[last])
   l.append(alist[first + (last-first)/2])
   med = int(np.median(l))

   if med == l[0]:
       medianIdx = first
   elif med == l[1]:
       medianIdx = last
   else:
       medianIdx = first + (last-first)/2

   assert med == alist[medianIdx],'Mismatch median'

#   print medianIdx, med, count

   alist[medianIdx], alist[first] = alist[first], alist[medianIdx]

   pivot = alist[first]
  
   i = first+1
   
   for j in range(i,last+1):
      if alist[j] < pivot:
         alist[i], alist[j] = alist[j], alist[i] 
         i += 1
   alist[first], alist[i-1] = alist[i-1], alist[first] 
   return i-1
count = 0
text_file = open("QuickSort.txt", "r")
lines = [int(i) for i in text_file.readlines()]

#lines = [10,9,8,7,6,4,5,2,3,1]
quickSort(lines)
print lines
#assert another.sort()==lines, 'Not Sorted'

print count
