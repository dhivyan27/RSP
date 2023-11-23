class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def length(self):
        length = 0
        curr = self.head.next
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def showlist(self):
        lst = []
        curr = self.head.next
        while curr is not None:
            lst.append(curr.data)
            curr = curr.next
        print(lst)

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.data
    

    def delete(self, data):
        curr = self.head

        if curr.next is None:
            print("List is empty")
            return None

        if curr.next.data == data:
            val = curr.next.data
            curr.next = curr.next.next
            return val
        
        while curr.next is not None:
            if curr.next.data == data:
                val = curr.next.data
                curr.next = curr.next.next
                return val
            curr = curr.next

        print("Data not found in list")
        return None



my_list = linkedlist()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.showlist()

