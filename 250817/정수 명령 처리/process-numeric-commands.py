N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class stack:
    def __init__(self):
        self.s = []
    
    def push(self, A):
        self.s.append(A)

    def empty(self):
        return not self.s

    def size(self):
        return len(self.s)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        
        return self.s.pop()
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        
        return self.s[-1]

s = stack()

for i in range(N):
    if command[i] == "push":
        s.push(value[i])
    
    elif command[i] == "size":
        print(s.size())
    
    elif command[i] == "empty":
        print(int(s.empty()))

    elif command[i] == "pop":
        print(s.pop())

    elif command[i] == "top":
        print(s.top())
        
    