from pylab import *
import networkx as nx

n = 1000
er = nx.erdos_renyi_graph(n, 0.01)
ws = nx.watts_strogatz_graph(n, 10, 0.01)
ba = nx.barabasi_albert_graph(n, 5)

Pk = [float(x) / n for x in nx.degree_histogram(er)]
domain = list(range(len(Pk)))
loglog(domain, Pk, '-', label = 'Erdos-Renyi')

Pk = [float(x) / n for x in nx.degree_histogram(ws)]
domain = list(range(len(Pk)))
loglog(domain, Pk, '--', label = 'Watts-Strogatz')

Pk = [float(x) / n for x in nx.degree_histogram(ba)]
domain = list(range(len(Pk)))
loglog(domain, Pk, ':', label = 'Barabasi-Albert')

xlabel('k')
ylabel('P(k)')
legend()
show()
