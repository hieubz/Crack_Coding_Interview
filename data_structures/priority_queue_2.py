class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def insert(self, node):
        # add new node
        if self.size() == 0:
            self.queue.append(node)
        else:
            # traverse the queue to find the right place
            for x in range(self.size()):
                if node.priority >= self.queue[x].priority:
                    if x == (self.size() - 1):
                        self.queue.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x + 1, node)
                    return True

    def delete(self):
        return self.queue.pop(0)

    def show(self):
        for x in self.queue:
            print(x)

    def size(self):
        return len(self.queue)
