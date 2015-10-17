def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
  if first<last:
   
     splitpoint = partition(alist,first,last)
     
     quickSortHelper(alist,first,splitpoint-1)
     quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   global count
   count += (last - first )
   pivot = alist[first]
  
   i = first+1
   
   for j in range(i,last+1):
      if alist[j] < pivot:
         temp = alist[i]
         alist[i] = alist[j]
         alist[j] = temp
         i += 1
   temp = alist[first]
   alist[first] = alist[i-1]
   alist[i-1] = temp

   return i-1
      
      
count = 0
text_file = open("QuickSort.txt", "r")
lines = [int(i) for i in text_file.readlines()]
#another = lines
#another.sort()
#print another
quickSort(lines)
print lines
#assert another.sort()==lines, 'Not Sorted'

print count
