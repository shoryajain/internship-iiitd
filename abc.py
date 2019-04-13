with open('temp4.txt') as f:
    routes = f.read().splitlines()

stops = list()

for x in routes:
    a = x[x.index('|')+1:x.rindex('|')]
    b = x[x.rindex('|')+1:]
    stops.append((a,b))

f = open('temp4.txt', "w")
for r in stops:
    f.write(r[0]+" "+r[1])
    f.write("\n")
f.close()