class node(object):
    
    def __init__(self,data):
        self.data=data
        self.nextnode=None

        
class linkedlist(object):
    
    
    def __init__(self):
        self.head=None
        self.size=0
        
    def insertatstart(self,data):
        self.size=self.size+1
        newnode=node(data)
        
        if self.head==None :
            self.head=newnode
            
        else:
            newnode.nextnode=self.head
            self.head=newnode
            
    def insertatend(self,data):
        self.size=self.size+1
        newnode=node(data)
        temp=self.head
        
        while (temp.nextnode != None):
            temp=temp.nextnode
            
        temp.nextnode=newnode
            
    def traverse(self):
        temp=self.head
        
        while temp != None :
            print temp.data
            temp=temp.nextnode
            
    def remove(self,data):
        if self.size==0 :
            print("nothing to remove")
            
        else:
            
            previousnode=None
            temp=self.head
            
            if temp.data==data :
                self.head=temp.nextnode
                self.size=self.size-1
            else:
                
                
                flag=0
                while temp.data != data:
                    
                    if temp.nextnode==None:
                        print("THIS ELEMENT IS NOT PRESENT \n")
                        flag=1
                        break
                    
                    previousnode=temp
                    temp=temp.nextnode
                    
                    
                    
                    
                if flag==0:
                    previousnode.nextnode=temp.nextnode
                    self.size=self.size-1


a=linkedlist()
print("\n============================\n 1.PRINT THE LIST \n 2.ADD ITEM AT BEGINNING \n 3.ADD ITEM AT END \n 4.REMOVE AN ITEM \n 5.TOTAL ITEMS IN LIST \n 6.EXIT \n")
while True:
    
    option=input("option>")
    
    
    if option == 1 :
        a.traverse()
        
    elif option == 2:
        data=input("VALUE TO ADD>")
        a.insertatstart(data)
        
    elif option == 3: 
        data=input("VALUE TO ADD>")
        a.insertatend(data)
        
    elif option==4:
        data=input("VALUE TO REMOVE>")
        a.remove(data)
    
    elif option==5:
        print "THERE ARE TOTAL "+str(a.size)+" ELEMENTS \n"
        
    elif option==6:
        break
        
    else:
        print("INVALID OPTION TRY AGAIN")
    
            
            