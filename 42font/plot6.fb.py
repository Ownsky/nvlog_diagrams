import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

fsnames = ['Ext-4', 'SPFS', 'NVLog (AS)', 'NOVA', 'NVLog'] # P2CACHE
clusters = ['Fileserver', 'Webserver', 'Varmail']

data = {
    'Fileserver' :  [12027.36,  10819.7,    5130.15,    3355.76,    11901.53],
    'Webserver' :   [22642.23,  21925.76,   22425.95,   11051.63,   23201.0],
    'Varmail' :     [714.06,    765.13,     2013.2,     2739.13,    2027.53],
}

colors = [
    '#bd8066', 
    '#a56cb6', 
    '#64ae8f', 
    '#8b9d4a', 
    '#5FA4D9', 
]
hatches = [
    '//', 
    'xx', 
    '++', 
    '--', 
    '\\\\', 
]

plt.rcParams['hatch.color'] = 'white'
plt.figure(figsize=(5, 2.5))
# plt.xlabel("Thread number")
plt.ylabel("Throughput (MB/s)")
plt.xticks(np.arange(3)*6+2, clusters)
plt.yscale('log')
h = []
for i, clust in enumerate(clusters):
    h = plt.bar(np.arange(5)+6*i, data[clust], color=colors, hatch=hatches, label=fsnames)

plt.legend(h, fsnames)
plt.savefig('filebench.pdf', bbox_inches='tight')