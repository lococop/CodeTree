n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    

class DDL:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
    
    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node

    
    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        
        return next_node

    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)

        elif node == self.begin():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
            

    def begin(self):
        return self.head

    def end(self):
        return self.tail


l = DDL()

for c in s:
    l.push_back(c)

it = l.end()

for i in range(m):
    com = commands[i]

    if com[0] == "L":
        if it != l.begin():
            it = it.prev
    elif com[0] == "R":
        if it != l.end():
            it = it.next
    elif com[0] == "D":
        if it != l.end():
            it = l.erase(it)

    else:
        l.insert(it, com[1])


it = l.begin()

while it != l.end():
    print(it.data, end="")
    it = it.next