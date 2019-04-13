import networkx as nx
# with open('temp2.txt') as f:
#     routes = f.read().splitlines()

# stops = list()

# for x in routes:
#     a = x[:x.index('|')]
#     b = x[x.index('|')+1:x.index(' ')+1]
#     c = x[x.index(' ')+1:]
#     stops.append((a,b,c))

# f = open('temp2.txt', "w")
# for r in stops:
#     f.write(r[0]+" "+r[1]+" "+r[2])
#     f.write("\n")
# f.close()

def all_paths(G, source, target, w):
    cutoff = len(G)-1
    visited = [source]
    stack = [iter(G[source])]
    weight = 0
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.pop()
        elif len(visited) < cutoff:
            if child == target:
                if (visited[-1],child) in G.nodes():
                    temp = G[visited[-1]][child]['weight']
                else:
                    temp = G[child][visited[-1]]['weight']
                if weight+temp <= w:
                    yield visited + [target]
            elif child not in visited:
                if (visited[-1],child) in G.nodes():
                    weight += G[visited[-1]][child]['weight']
                else:
                    weight += G[child][visited[-1]]['weight']
                visited.append(child)
                stack.append(iter(G[child]))
        else: 
            if child == target or target in children:
                if (visited[-1],child) in G.nodes():
                    temp = G[visited[-1]][child]['weight']
                else:
                    temp = G[child][visited[-1]]['weight']
                if weight+temp <= w:
                    yield visited + [target]
            stack.pop()
            visited.pop()

G = nx.Graph()
G.add_edge(1,2,weight=2)
G.add_edge(2,3,weight=0)
G.add_edge(3,4,weight=0)
G.add_edge(1,4,weight=0)

print([p for p in all_paths(G,source=1,target=2, w=0)])
print([p for p in all_paths(G,source=1,target=2, w=1)])
print([p for p in all_paths(G,source=1,target=2, w=2)])
print([p for p in all_paths(G,source=1,target=2, w=3)])