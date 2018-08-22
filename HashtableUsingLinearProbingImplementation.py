
# coding: utf-8

# In[1]:


class Hashtable:
    def __init__(self):
        self.size=10
        self.key=[None]*self.size
        self.value=[None]*self.size
        
    def hashfunction(self,key):
        sum=0
        for pos in range(len(key)):
            sum=sum+ord(key[pos])
            
        return sum%self.size

#insert method    
# first we assume that collision occured so we loop until we find an emptyplace
#while looping we also check weather that key already exist 
#if yes we update the value and exit
#We loop according to linear probing implementation and increment the index by 1
#when we come out of while (without invoking return present inside )it means 
#we have reached an empty space and we update the value    
    
    def insert(self,key,data):
        index=self.hashfunction(key)

        while self.key[index] != None:
            if self.key[index]==key:
                self.value[index]=data
                return
            
            index=(index+1)%self.size
            
        self.key[index]=key
        self.value[index]=data
            
    def get(self,key):
        index=self.hashfunction(key)
        
        while self.key[index] != None :
            if self.key[index]==key:
                return self.value[index]
            index=(index+1)%self.size
            
        return None
        
        
table=Hashtable()
table.insert('apple',10)
table.insert('orange',20)
table.insert('car',30)
table.insert('table',40)
print table.get('car')

    

