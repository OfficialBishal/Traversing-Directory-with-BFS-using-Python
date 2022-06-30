import os
basedir = 'graph_project_start'
destination = input("Enter the file/folder name you want to search (include extension for files): ")

breadth = (os.listdir(basedir))

queue = []

visited = []

queue.append(basedir)

# Initiating loop
while (len(queue) != 0):
    active_node = queue.pop(0)
    visited.append(active_node)
    file_name = active_node.split('/')
    if (file_name[-1] == destination):
        print(f"\nVisited: {visited}")
        print(f"Queue: {queue}")
        break
    if (os.path.isdir(active_node)):
        innernode = os.listdir(active_node)
        for node in innernode:
            if node not in visited:
                queue.append(f'{active_node}/{node}')

    print(f"\nVisited: {visited}")
    print(f"Queue: {queue}")

if (destination):
    print(f'\nThe path of the destination is: {visited[-1]}')

