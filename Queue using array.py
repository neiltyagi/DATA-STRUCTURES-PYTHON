class queue:
    def __init__(self):
        self.queue=[]
        
    def isempty(self):
        return self.queue==[]
        
        
    def enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue.data[0]
    
    def size(self):
        return len(self.queue)
    
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print (q.size())
print "Dequeue: ",q.dequeue()
print "Dequeue: ",q.dequeue()
print q.size()