class PriorityQueue:
    def __init__(self):

        self.heap = []


    def front(self):

        if self.isEmpty():
            return ValueError("heap is empty")
        
        return self.head[0]
    
    
    def push(self,value):
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)


    def pop(self):

        if self.isEmpty():
            return ValueError("heap is empty")
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] #swap top of heap with bottom right
        popped_value = self.heap.pop()
        self.bubble_down(0)
        return popped_value


    def isEmpty(self):
        return len(self.heap) == 0
    

    def bubble_up(self,index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.bubble_up(parent_index)



    def bubble_down(self,index):
        smallest = index
        left_child= index * 2 + 1
        right_child = index * 2 + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)       



pq = PriorityQueue()