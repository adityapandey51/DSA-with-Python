class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.right=None
        self.left=None
class doubly:
    def __init__(self) -> None:
        self.head=None

    def isEmpty(self):
        return True if self.head==None else False
    def insert_b(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            self.head.left=newNode
            newNode.right=self.head
            self.head=newNode
    def insert_e(self,data):
        newNode=Node(data)
        tmp=self.head
        while tmp.right:
            tmp=tmp.right
        newNode.left=tmp
        tmp.right=newNode
    def insert_m(self,element,data):
        newNode=Node(data)
        tmp=self.head
        while tmp:
            if tmp.data==element:
                break
            tmp=tmp.right
        newNode.right=tmp.right
        tmp.right.left=newNode
        tmp.right=newNode
        newNode.left=tmp
    def delete_b(self):
        if self.head==None:
            print("list is empty")
        else:
            self.head=self.head.right
            self.head.left=None
    def delete_e(self):
        tmp=self.head
        while tmp.right.right:
            tmp=tmp.right
        tmp.right.left=None
        tmp.right=None
    def delete_m(self,data):
        tmp=self.head
        while tmp.right:
            if tmp.right.data==data:
                break
            tmp=tmp.right
        a=tmp.right.right
        a.left=tmp
        tmp.right=a
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            tmp=self.head
            while tmp:
                print(tmp.data,"<-->",end="")
                tmp=tmp.right
            print()
s=doubly()
s.insert_b(5)
s.insert_e(6)
s.insert_m(5,5.5)
s.display()
s.insert_e(7)
s.delete_m(6)
s.display()
s.delete_e()
s.display()

    
