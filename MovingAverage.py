from CircularBuffer import CircularBuffer

class MovingAverage(CircularBuffer):

    def __init__(self):
        '''Store buffer in given storage'''
        CircularBuffer.__init__(self, size)
        self.total = 0
    
    def getAverage(self):
        '''Moving Average'''
        if self.count == 0:
            return 0
        return self.total/self.count
    
    def remove(self):
        '''Removes oldest value from a non-empty buffer'''
        removed = CircularBuffer.remove(self)
        self.total -= removed
        return removed

    def add(self, value):
        '''Add value to buffer, overwrite as needed'''
        if self.isFull():
            delta = -self.buffer[self.low]
        else:
            delta = 0
        delta +=value
        self.total += delta
        CircularBuffer.add(self,value)
    
    def __repr__(self):
        if self.isEmpty():
            return 'ma:[]'
        return 'ma:[' + ','.join(map(str,self)) + ']'