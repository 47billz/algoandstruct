from LinkedList import Node

class QueueLinkedList:
    def __init__(self,*start):
        self.head = None
        self.tail = None
    
    def append(self, value):
        '''Add value at the end of Queue'''
        newNode = Node(value,None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode    #update the end with new node
            self.tail = newNodes        #update the tail pointer
    
    def isEmpty():
        '''Determine if the Queue is empty'''
        return self.head == None
    
    def pop(self):
        '''Remove the first element O(1)'''
        if self.head == None:
            raise Exception ("Empty List")
        
        value = self.head.value
        self.head = self.head.next
        if self.head is None: #Make sure to update the tail pointer
            self.tail = None
        return value
    
    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next
    
    def __repr__(self):
        if self.head == None:
            return 'Queue:[]'
        return 'Queue:[' + ','.join(map(str,self)) + ']'