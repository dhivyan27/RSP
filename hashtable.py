class HashTable:

    def __init__(self):
        self.size = 10
        self.table = [[] for i in range(self.size)]

    
    def hashfunction(self,key):
        total = 0
        for char in key:
            total += ord(char)

        return sum % self.size

    

    def insert(self,value):
        hashkey =  self.hashfunction(value)
        bucket = self.table[hashkey]

        if key in bucket:
            return
        
        else:
            bucket.append(key)


    def remove(self,value):
        hashkey =  self.hashfunction(value)
        bucket = self.table[hashkey]

        bucket.remove(value)


    def contains(self,value):
        hashkey =  self.hashfunction(value)
        bucket = self.table[hashkey]

        return value in bucket



hash_table = HashTable()


        