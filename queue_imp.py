class queue:
    def __init__(self,capacity) -> None:
         self.queue=[]
         self.capacity=capacity
         self.front=self.rear=-1
    def isFull(self):
         if self.capacity-1==self.rear:
              return True
         else:
              return False
    def enqueue(self,item):
        if self.isFull():
              print("queue is full")
        elif (self.rear==-1 & self.front==-1):
             self.queue.append(item)
             self.rear=self.front=0
        else:
             self.queue.append(item)
             self.rear+=1
             
    def dequeue(self):
         if self.isEmpty():
              print("queue is empty")
         elif (self.front==0 & self.rear==0):
              self.queue.pop(0)
              self.front=self.rear=-1
              
         else:
              self.queue.pop(0)
              self.rear-=1
    def isEmpty(self):
         if self.front==-1 and self.rear==-1:
              return True
         else:
              False
    def display(self):
         print(self.queue)

s=queue(5)
s.dequeue()
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.enqueue(6)
s.display()
    