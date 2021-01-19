import heapq

l = [5, 7, 9, 2, 1, 10]

heapq.heapify(l)
print(list(l))

heapq.heappush(l, 15)
print(list(l))

print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))
print(l)