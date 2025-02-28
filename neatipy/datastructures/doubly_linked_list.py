from node import Node

class DoublyLinkedList():
    def __init__(self,max_size:int=128)->None:
        self._max_size=max_size
        self.size=0
        self.head=None
        self.tail=None
    
    def is_empty(self)->bool:
        return self.head is None
    

    def remove_from_tail(self)->None:
        new_tail=self.tail.prev
        if new_tail is None:
            self.head=None
            self.tail=None
            self.size-=1
            return
        self.tail=new_tail
        self.tail.next=None
        self.size-=1
        

    def insert_to_head(self,node:Node)->None:
        if self.is_empty():
            self.head=node
            self.tail=self.head
            return
        old_head=self.head
        old_head.prev=node
        self.head=node
        self.head.next=old_head
        self.size+=1
        if self.size>self._max_size:
            self.remove_from_tail()