from typing import Any


class Node:

    def __init__(self):
        self.children = {}
        self.isComplete = False



class Trie:
    
    def __init__(self,root):
        self.root = Node


    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]

        node.isComplete = True


    def search(self,word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.isComplete
    

    def prefix(self,prefix):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
