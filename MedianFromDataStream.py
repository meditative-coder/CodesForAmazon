import heapq


class Heap:
    def __init__(self):
        self.small = []
        self.large = []
    
    def add(self,num):
        heapq.heappush(self.small, -1*num)
        #heapq.heappush(self.small, -1*num)
        if self.small and self.large and -1*self.small[0] > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large,-1*val)
        if len(self.small)>len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
        if len(self.large)>len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
    
    def find_median(self):
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        return (-1*self.small[0]+self.large[0])/2

if __name__=="__main__":
    heap = Heap()
    heap.add(1)
    heap.add(2)
    print(heap.find_median())
    heap.add(3)
    print(heap.find_median())
    heap.add(4)
    print(heap.find_median())