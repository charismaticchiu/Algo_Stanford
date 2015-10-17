# Priority dictionary using binary heaps
# David Eppstein, UC Irvine, 8 Mar 2002
 
from __future__ import generators
 
class priorityDictionary(dict):
    ##
    # Initialize priorityDictionary by creating binary heap
    # of pairs (value,key).  Note that changing or removing a dict entry will
    # not remove the old pair from the heap until it is found by smallest() or
    # until the heap is rebuilt.
    def __init__(self):
        self.__heap = []
        dict.__init__(self)

    ##
    # Find smallest item after removing deleted items from heap.
    def smallest(self):

        if len(self) == 0:
            raise IndexError, "smallest of empty priorityDictionary"
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and \
                        heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break

                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]
    
    ##
    # Create destructive sorted iterator of priorityDictionary.
    def __iter__(self):
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x

                del self[x]
        return iterfn()
    
    ##
    # Change value stored in dictionary and add corresponding
    # pair to heap.  Rebuilds the heap if the number of deleted items grows
    # too large, to avoid memory leakage.
    def __setitem__(self,key,val):
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()  # builtin sort likely faster than O(n) heapify
        else:

            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint-1)//2]:

                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair
    
    ##
    # Reimplement setdefault to call our customized __setitem__.
    def setdefault(self,key,val):
        if key not in self:
            self[key] = val
        return self[key]
