class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)

            else:
                self.left.insert(data)

        elif data > self.data:
            if self.right is None:
                self.right = Node(data)

            else:
                self.right.insert(data)


    def inordertraversal(self):
        if self.left:
            self.left.inordertraversal()
        
        print(self.data)

        if self.right:
            self.right.inordertraversal()

        
    def preordertraversal(self):

        print(self.data)

        if self.left:
            self.left.preordertraversal()
        
        if self.right:
            self.right.preordertraversal()

    def postordertraversal(self):
            
        if self.left:
            self.left.postordertraversal()
        
        if self.right:
            self.right.postordertraversal()

        print(self.data)


    def find(self,data):

        if self.data == data:
            return True
        
        elif data > self.data:
            if self.right is None:
                return False
            else:
                self.right.find(data)

        else:
            if self.left is None:
                return False
            else:
                self.left.find(data)


