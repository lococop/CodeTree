commands = input()

# Please write your code here.
first_x, first_y = 0, 0
x, y = 0, 0

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

move_dir = 3
time = 0
Is_match = False

for elem in commands:
    if elem == 'F':
        x, y = x + dxs[move_dir], y + dys[move_dir]
    
    elif elem == 'R':
        move_dir = (move_dir + 1) % 4
    
    elif elem == 'L':
        move_dir = (move_dir + 3) % 4
    
    time += 1
    if x == first_x and y == first_y:
        Is_match = True
        break
    

if Is_match:
    print(time)
else:
    print(-1)
        
