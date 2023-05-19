class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None

class linkedList:
    def __init__(self) -> None:
        self.head=None
    def isEmpty(self):
        return True if self.head==None else False
    def insert_b(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.ref=self.head
            self.head=newNode
    def insert_e(self,data):
        newNode=Node(data)
        tmp=self.head
        while tmp.ref:
            tmp=tmp.ref
        tmp.ref=newNode
    def insert_m(self,element,data):
        newNode=Node(data)
        tmp=self.head
        while tmp:
            if tmp.data==element:
                break
            tmp=tmp.ref
        x=tmp.ref
        newNode.ref=x
        tmp.ref=newNode
    def display(self):
        tmp=self.head
        while tmp:
            print(tmp.data,"-->",end=" ")
            tmp=tmp.ref
        print()
    def delete_b(self):
        if self.head==None:
            print("linkedList is empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        tmp=self.head
        while tmp.ref.ref:
            tmp=tmp.ref
        tmp.ref=None
    def delete_m(self,data):
        tmp=self.head
        while tmp.ref:
            if tmp.ref.data==data:
                break
            tmp=tmp.ref
        tmp.ref=tmp.ref.ref
        
s=linkedList()
s.insert_b(5)
s.insert_e(6)
s.insert_m(5,5.5)
s.display()
s.insert_e(7)
s.delete_m(6)
s.display()
s.delete_end()
s.display()


