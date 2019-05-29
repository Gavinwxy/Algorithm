from collections import defaultdict

file = open('dijkstra_test_input.txt', 'r')
data = file.readlines()

# Graph initialization
graph = defaultdict(dict)
for line in data:
    items = line.split()
    node, connects = int(items[0]), items[1:]
    for connect in connects:
        info = connect.split(',')
        v = int(info[0])
        length = int(info[1])
        graph[node][v] = length

# Nodes set initialization
vset = {}
vset[1] = 0

oset = list(graph.keys())[1:]

while oset:
    v_select = None
    min_len = 10000000
    for key1 in vset.keys():
        for key2 in graph[key1]:
            if key2 not in vset:
                len_cal = vset[key1] + graph[key1][key2]
                if len_cal < min_len:
                    min_len = len_cal
                    v_select = key2
    vset[v_select] = min_len
    oset.remove(v_select)


targets = [7,37,59,82,99,115,133,165,188,197]
solve = []
for t in targets:
    solve.append(vset[t])

print(solve)