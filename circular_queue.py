class circular_queue:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.queue=[None for i in range(capacity)]
        self.rear=self.front=-1
    def enqueue(self,item):
        if (self.rear+1)%self.capacity==self.front:
            print("queue is full")
        elif (self.rear==-1 and self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=item
        else:
            self.rear=(self.rear+1)%self.capacity
            self.queue[self.rear]=item
    def dequeue(self):
        if (self.front==-1 and self.rear==-1):
            print("queue is empty")
        elif (self.front==0 and self.rear==0):
            x=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return x
        
        elif (self.front==self.rear):
            x=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return x

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return temp
    def display(self):
        if self.front==-1:
            print("queue is empty")
        elif (self.rear+1)%self.capacity==self.front:
            print("queue is full")
        elif (self.rear>=self.front):
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            for i in range(self.front,self.capacity):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()

s=circular_queue(3)
s.enqueue(1)
s.enqueue(2)
s.display()
s.dequeue()
s.display()
s.dequeue()
s.display()
