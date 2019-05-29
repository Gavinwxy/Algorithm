# -*- coding: utf-8 -*-

import heapq
from collections import defaultdict

file = open('dijkstra_test_input.txt','r')
data = file.readlines()

oset = []
g = defaultdict(list)
for line in data:
    info = line.split()
    v = int(info[0])
    oset.append(v)
    for ele in info[1:]:
        node = ele.split(',')
        g[v].append((int(node[0]), int(node[1])))


heap = [(0, 1)]
resset = {}
while oset:
    dist, node = heapq.heappop(heap)
    if node in oset:
        resset[node] = dist
        for v, l in g[node]:
            heapq.heappush(heap, (dist+l, v))
        oset.remove(node)

targets = [7,37,59,82,99,115,133,165,188,197]
solve = []
for t in targets:
    solve.append(resset[t])
