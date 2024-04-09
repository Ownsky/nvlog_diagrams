import matplotlib.pyplot as plt
import numpy as np

fsnames = ['Ext-4', 'SPFS', 'NOVA', 'NVPC'] # P2CACHE
clusters = ['Fileserver', 'Webserver', 'Varmail']

data = {
    'Fileserver' :  [12027.36,  10819.7,    3355.76,    11901.53],
    'Webserver' :   [22642.23,  21925.76,   11051.63,   22463.66],
    'Varmail' :     [714.06,    765.13,     2739.13,    2027.53],
}

colors = [
    '#bd8066', 
    '#a56cb6', 
    '#8b9d4a', 
    '#5FA4D9', 
]
hatches = [
    '//', 
    'xx', 
    '--', 
    '\\\\', 
]

plt.rcParams['hatch.color'] = 'white'
plt.figure(figsize=(6, 3))
# plt.xlabel("Thread number")
plt.ylabel("Throughput (MB/s)")
plt.xticks(np.arange(3)*5+1.5, clusters)
plt.yscale('log')
h = []
for i, clust in enumerate(clusters):
    h = plt.bar(np.arange(4)+5*i, data[clust], color=colors, hatch=hatches, label=fsnames)

plt.legend(h, fsnames)
plt.savefig('plot5.pdf', bbox_inches='tight')