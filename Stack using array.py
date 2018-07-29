class stack:
    
    def __init__(self):
        self.stack=[]
        
    def isempty(self):
        return self.stack==[]
    
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
        
    
s=stack()
print s.isempty()
s.push(1)
s.push(2)
s.push(4)
print s.peek()
print s.size()
print s.isempty()

