# Link list noad creation
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None



class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval







# Creating nodes
e1= Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")




# Creating link list
e1.nextval = e2
e2.nextval = e3





# Defining link list
list = SLinkedList()
list.headval = e1







""" puting the head in another veriable. Don't create new node just refers to 
the address where it belong"""
listTrav = list.headval

# Traversing all node one by one
while listTrav!=None:
    print(listTrav.dataval)
    listTrav=listTrav.nextval
    






#inserting at the beginning
e4=Node("Sun")
e4.nextval=list.headval
list.headval=e4
list.listprint()






#Inserting a Node at the end
e4 = Node("Thu")
if list.headval is None:
    list.headval = e4
else:
    listTrav = list.headval
    while(listTrav.nextval):
        listTrav = listTrav.nextval
    listTrav.nextval=e4
list.listprint()







#Inserting a Node after a fix node
listTrav = list.headval
while listTrav.dataval!="Mon":
    print(listTrav.dataval)
    listTrav=listTrav.nextval
     
    
print("ok")
e4=Node("Fri")
e4.nextval=listTrav.nextval
listTrav.nextval=e4

list.listprint()








#Inserting a Node before a fix node
listTrav = list.headval
# 'prev' the previous node  
prev= None
while listTrav.dataval!="Mon":
    prev = listTrav
    #print(listTrav.dataval)
    listTrav=listTrav.nextval
     
    
print("ok - -")
e4=Node("Wed")


if prev!=None:
    #if it is not first node
    e4.nextval=prev.nextval
    prev.nextval=e4
else:
    #if it is the first node
    e4.nextval=list.headval
    list.headval=e4

list.listprint()
    








#Removing  a node
listTrav = list.headval
# 'prev' the previous node  
prev= None
while listTrav.dataval!="Sun":
    prev = listTrav
    #print(listTrav.dataval)
    listTrav=listTrav.nextval
     
if prev==None:
    # if it is first node
    list.headval=list.headval.nextval
else:
    # if is is not first node
    prev.nextval=listTrav.nextval

list.listprint()
    
    
    
    
    
    
    
    
    
    
    