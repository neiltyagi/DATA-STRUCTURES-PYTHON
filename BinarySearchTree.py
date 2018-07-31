class nodeoftree(object):
    def __init__(self,data):
        self.data=data
        self.rightchild=None
        self.leftchild=None

        
class binarysearchtree(object):
    
    def __init__(self):
        self.root=None
        
    def insert(self,data):
            
        if self.root==None:
            self.root=nodeoftree(data)
            
        else:
            self.insertnode(data,self.root)
# O(logN)   if the tree is balanced !!!!!!!!!!!!!  --> for unbalanced tree it can reduced to O(N) --> AVL RBT are needed !!!!!
            
    def insertnode(self,data,node):
            
        if data<node.data:
            if node.leftchild != None:
                self.insertnode(data,node.leftchild)
                
            else:
                newnode=nodeoftree(data)
                node.leftchild=newnode
    
           
        else:
            if node.rightchild != None:
                self.insertnode(data,node.rightchild)
                
            else:
                newnode=nodeoftree(data)
                node.rightchild=newnode
                
                
                
    def getminvalue(self):
        if self.root.leftchild==None:
            return self.root.data
        else:
            temp=self.root.leftchild
            while temp.leftchild != None:
                temp=temp.leftchild
            return temp.data   
        
        
    def getmaxvalue(self): 
        if self.root.rightchild==None:
            return self.root.data
        else:
            temp=self.root.rightchild
            while temp.rightchild != None:
                temp=temp.rightchild
            return temp.data
     
    
    def traverse(self):
		if self.root:
			self.traverseInOrder(self.root);
			
			# O(N)
    def traverseInOrder(self, node):
	
		if node.leftchild:
			self.traverseInOrder(node.leftchild);
			
		print("%s " % node.data);
		
		if node.rightchild:
			self.traverseInOrder(node.rightchild);
            
            
            
    def remove(self,data):
        parent=None
        temp=self.root
        
        while temp.data != data:
            if temp.data>data:
                parent=temp
                temp=temp.leftchild
            else:
                parent=temp
                temp=temp.rightchild
        
        
        if (temp.rightchild == None) and (temp.leftchild == None): #if temp is leaf node
            print "removing leafnode"
            if parent.rightchild==temp:
                parent.rightchild=None
                del temp
            elif parent.leftchild==temp:
                parent.leftchild=None
                del temp
                
        elif (temp.rightchild != None) and (temp.leftchild == None): #if temp has right single child
            print "removing node with right single child"
            if parent.rightchild==temp:
                parent.rightchild=temp.rightchild
                del temp
            elif parent.leftchild==temp:
                parent.leftchild=temp.rightchild
                del temp
            
        elif (temp.leftchild != None) and (temp.rightchild == None): #if temp has left single child
            print "removing node with left single child"

            if parent.rightchild==temp:
                parent.rightchild=temp.leftchild
                del temp
            elif parent.leftchild==temp:
                parent.leftchild=temp.leftchild
                del temp
        
        
        elif (temp.leftchild != None) and (temp.rightchild != None): #if temp has both children
            
            print "removing node with both children"

            
            parent=temp
            temp1=temp.leftchild #finding largest item in left subtree
            
            while temp1.rightchild != None:
                parent=temp1
                temp1=temp1.rightchild
            
            temp.data=temp1.data
            if temp1.leftchild != None:
                parent.rightchild=temp1.leftchild
                del temp1
                
            else:
                parent.leftchild = None
                del temp1
            
            
            
            
            
                
        

        
tree=binarysearchtree()
tree.insert(59)
tree.insert(93)
tree.insert(82)
tree.insert(1)
tree.insert(99)
tree.insert(44)
tree.insert(33)
tree.insert(9)

print tree.getminvalue()
print tree.getmaxvalue()
tree.traverse()
print "\n \n"
tree.remove(59)
tree.traverse()