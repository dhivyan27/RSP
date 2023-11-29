import heapq

class PriorityQueue:
    def __init__(self):

        self.heap = []


    def front(self):

        if self.isEmpty():
            return ValueError("heap is empty")
        
        return self.head[0]
    
    
    def push(self,value):
        return heapq.heappush(self.heap, value)


    def pop(self):

        if self.isEmpty():
            return ValueError("heap is empty")
        return heapq.heapop(self.heap)
    

    def isEmpty(self):
        return len(self.heap) == 0
    


pq = PriorityQueue()