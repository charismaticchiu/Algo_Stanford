def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
	
       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   global count
   count += (last - first)
   
   temp = alist[last]
   alist[last] = alist[first]
   alist[first] = temp
   
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
   #print count 
   return i-1
count = 0
text_file = open("QuickSort.txt", "r")
lines = [int(i) for i in text_file.readlines()]
#another = lines
#another.sort()
#print another

#lines = [1,3,5,7,9,2,4,6,10,8]
quickSort(lines)
print lines
#assert another.sort()==lines, 'Not Sorted'

print count
