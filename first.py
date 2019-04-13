import networkx as nx

def all_paths(G, source, target, vazan):
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
                if weight+temp <= vazan:
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
                if weight+temp <= vazan:
                    yield visited + [target]
            stack.pop()
            visited.pop()

with open('temp.txt') as f:
    routes = f.read().splitlines()

main = nx.Graph()
for j in routes:
    fi = 'temp('+j+').txt'
    with open(fi) as f:
        lines = f.read().splitlines()
    i = 1
    G = nx.Graph()
    while i < len(lines):
        if i != len(lines):
            G.add_edge(lines[i-1],lines[i],weight=0)
        i = i + 1
    main = nx.union(G,main, rename=(j+'-',None))

with open('temp2.txt') as f:
    temporary = f.read().splitlines()

for x in temporary:
    a = x[:x.index(' ')]
    b = x[x.index(' ')+1:x.index('  ')]
    c = x[x.index('  ')+2:]
    main.add_edge(a+'-'+c,b+'-'+c,weight=1)

with open('temp3.txt') as f:
    temporary = f.read().splitlines()

stop_routes = dict()
for x in temporary:
    a = x[:x.index(' ')+1]
    b = x[x.rindex(' ')+1:]
    stop_routes.setdefault(a,[]).append(b)

with open('temp4.txt') as f:
    temporary = f.read().splitlines()

stops = dict()
for x in temporary:
    a = x[:x.index(' ')+1]
    b = x[x.index(' ')+1:]
    stops.setdefault(a,0)
    stops[a] = b


