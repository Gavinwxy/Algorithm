from collections import defaultdict

class Graph(object):
    def __init__(self, connections, directed=False):
        self.graph = defaultdict(set)
        self._directed = directed
        self.node_info = {}
        self.node_label = 0
        self.add_connections(connections)

    
    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        if node1 not in self.graph:
            self.node_info_init(node1)
        if node2 not in self.graph:
            self.node_info_init(node2)

        self.graph[node1].add(node2)
        if node2 not in self.graph:
            self.graph[node2] = set()
        if not self._directed:
            self.graph[node2].add(node1)

    def node_info_init(self, node):
        self.node_info[node] = {'visited':0, 'topo_order':None, 'scc_num':None}
    
    def topo_order_set(self, node, order):
        self.node_info[node]['topo_order'] = order

    def get_topo_sort(self):
        info = sorted(self.node_info)
            
    def topo_sort(self):
        V = len(self.graph.keys())
        self.node_label = V
        nodes = list(self.graph.keys())
        for v in nodes:
            if self.node_info[v]['visited'] == 0:
                self.dfs_topo(v)  

    def dfs_topo(self, v):
        self.node_info[v]['visited'] = 1
        for w in self.graph[v]:
            if self.node_info[w]['visited'] == 0:
                self.dfs_topo(w)
        self.topo_order_set(v, self.node_label)
        self.node_label -= 1
    

if __name__ == "__main__":
    file = open("SCC_test_input.txt", "r")
    data = file.readlines()

    connect = []
    connect_re = []
    for line in data:
        items = line.split()
        connect.append((items[0], items[1]))
        connect_re.append((items[1], items[0]))
    
    scc = []
    g = Graph(connect, directed = True)
    g_re = Graph(connect_re, directed = True)

    # Topological sort on reverse graph
    g_re.topo_sort()
    scc_order = []
    for topo_order in range(1,len(g.graph.keys())):
        for key in list(g_re.graph.keys()):
            if g_re.node_info[key]['topo_order'] == topo_order:
                scc_order.append(key)
    
    # DFS on forward graph
    scc_num = 0
    stack = []
    for v in scc_order:
        scc_num += 1
        if g.node_info[v]['visited'] == 1:
            continue
        stack = [v]
        while stack:
            stack_node = stack.pop()
            if g.node_info[stack_node]['visited'] == 0:
                g.node_info[stack_node]['visited'] = 1
                g.node_info[stack_node]['scc_num'] = scc_num
                for node in g.graph[stack_node]:
                    stack.append(node)
        

    for node in list(g.graph.keys()):
        scc.append(g.node_info[node]['scc_num'])
    
    scc = list(set([scc.count(x) for x in scc]))
    print(scc[:5])