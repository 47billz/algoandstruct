class Node:

    def __init__(self,value, tail=None):
        self.value = value
        self.next = tail

class LinkedList():
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_)
    
    def prepend(self, value):
        '''Add value to front of list O(1).'''
        self.head = Node(value,self.head)

    def remove(self, value):
        '''Remove a value from list.'''
        n = self.head   #keep track of the current element
        last = None     #keep track of the previous elements
        while(n!=None):
            if n.value == value:
                if last == None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            last = n    #move current to previous
            n = n.next  #move forward
        return False

    
    def pop(self):
        '''Remove the first element O(1)'''
        if self.head == None:
            raise Exception ("Empty List")
        
        value = self.head.value
        self.head = self.head.next
        return value
    
    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next
    
    def __repr__(self):
        if self.head == None:
            return 'list:[]'
        return 'list:[' + ','.join(map(str,self)) + ']'