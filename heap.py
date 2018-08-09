class Heap(object):
    
    MAX_SIZE=10
    
    def __init__(self):
        self.heap=[0]*Heap.MAX_SIZE
        self.currentposition=-1
    
    
    def insert (self,data):
        
        if self.isfull():
            print "heap is already full cannot add more elements"
            return
        
    
        self.currentposition += 1
        self.heap[self.currentposition]=data
        self.fixup(self.currentposition)
        print self.heap
        
    
    
        
    def fixup(self,index):
        parent=(index-1)/2
        
        while parent >= 0 and self.heap[index] > self.heap[parent]:
            temp=self.heap[index]
            self.heap[index]=self.heap[parent]
            self.heap[parent]=temp
            index=parent
            parent=(index-1)/2
    
    
    
    
    def isfull (self):
        if self.currentposition==9:
            return True
        else:
            return False
        
        
        
    def heapsort(self):
        
        while (self.currentposition >= 0):
            print self.heap[0]
            self.heap[0]=self.heap[self.currentposition]
            self.heap[self.currentposition]=0
            self.currentposition = self.currentposition - 1
            self.heapify()
         
    def heapify(self):
        index=0
        
        while True:
            lchild=(2*index)+1
            rchild=(2*index)+2
            if lchild<=self.currentposition and rchild<=self.currentposition:  #rchild and lchild both exist
                

                maxchildindex = lchild if self.heap[lchild] > self.heap[rchild] else rchild   #chechking maximum of 2 childern

                if self.heap[index]<self.heap[maxchildindex]:      #if maxchild greater than parnet node than swap
                    self.swap(index,maxchildindex)
                    index=maxchildindex

                else:
                    break

            elif lchild<=self.currentposition :    #only lchild exist
                if self.heap[index]<self.heap[lchild]:
                    self.swap(index,lchild)
                    index=lchild
                else:
                    break
                    
                    
            elif rchild<=self.currentposition:   #only rchild exist
                if self.heap[index]<self.heap[rchild]:
                    self.swap(index,lchild)
                    index=rchild
                else:
                    break
                
            else:
                break
    
        
    def swap(self,a,b):
        temp=self.heap[a]
        self.heap[a]=self.heap[b]
        self.heap[b]=temp
        
    
        
    
a=Heap()
a.insert(4)
a.insert(5)
a.insert(1)
a.insert(3)
a.insert(34)
a.insert(33)
a.insert(44)
a.insert(39)
a.insert(7)
a.insert(45)
a.insert(99)
a.heapsort() 

        
a.insert(33)
a.insert(22)