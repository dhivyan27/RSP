class Vector:
    def __init__(self):

        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity


    def front(self):
        if self.isEmpty():
            return ValueError("Vector is Empty")
        return self.array[0]
    
    def push(self,val):

        if self.size + 1 > self.capacity:
            self.resize(self.capacity * 2)

        self.array[self.size] = val
        self.size += 1


    def pop(self):
        if self.isEmpty():
            return ValueError("Vector is Empty")

        output = self.array[self.size - 1]
        self.size -= 1
        return output
    
    def isEmpty(self):
        return self.size == 0
    
    def resize(self,capacity):
        new_array = [None] * capacity
        for i in range(self.array):
            new_array[i] =  self.array[i]
        
        self.array = new_array
        self.capacity = capacity




vector = Vector()