"""
Priority queue: a data structure - queue - where each data/value in the queue
has a certain priority.

Applications:
+ Job scheduling algorithms
+ CPU and Disk scheduling
+ managing resources that are shared among different processes

Key differences between Priority Queue and Queue
- in Queue, there is only FIFO principle
- in Priority Queue, element with highest priority will be dequeued first.

"""


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i

            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print("fuck")
            exit()
