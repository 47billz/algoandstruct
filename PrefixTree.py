WordKey = '\n' #any character not in 'a' .. 'z'  -> represent actual words in the dictionary

class PrefixTree:
    def __init__(self):
        self.head = {}
    
    def add(self, value):
        ''' add value to prefix tree '''
        d = self.head
        while len(value) > 0:   #As long as I have anything to add
            c =value[0]:        #Take the first character in value
            if c not in d:      #Check if the character is in dictionary
                d[c] = {}       #if not, make c a key to a new dictionary
                value = value[1:]    #move to the next charactor
        if WordKey in d:
            return False
        d[WordKey] = True
        return True