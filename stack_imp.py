def create_stack():
    stack=[]
    return stack
def isEmpty_stack(stack):
    if len(stack)==0:
        return True
    else:
        return False
def push(stack,item):
    stack.append(item)
    print(item,"has been pushed into the stack")
def pop(stack,item):
    if isEmpty_stack(stack):
        print("stack underflow")
    else:
        x=stack.pop()
        print("the popped element is",x)
def peek(stack):
    if isEmpty_stack(stack):
        print("stack underflow")
    else:
        print("the peek of stack is",stack[-1])
def display(stack):
    print(stack)
