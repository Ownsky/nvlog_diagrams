import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

data_64b = {
    "sys":  [20.5, 28.1, 45.9, 83.9],
    "real": [21.0, 47.0, 83.5, 136.1]
}

data_4k = {
    "sys":   [15.0, 22.0, 23.4, 45.0],
    "real":  [34.2, 38.1, 42.6, 176.5]
}

data = {
    "64B": data_64b,
    "4KB": data_4k
}

index = ["2GB", "4GB", "8GB", "16GB"]

# df_64b = pd.DataFrame(data_64b, index = index)
# df_4k = pd.DataFrame(data_4k, index = index)

for d in data:
    plt.rcParams['hatch.color'] = 'white'
    plt.figure(figsize=(5, 2.5))
    plt.ylabel("Time (s)")
    plt.xticks(np.arange(4)*4+1, index)
    plt.title(d+' IO Size')
    # plot scan (sys)
    h = plt.bar(np.arange(4)*4, data[d]["sys"], color='#8b9d4a', hatch='--', label="Scan")
    # plot io (real-sys)
    h = plt.bar(np.arange(4)*4+1, np.array(data[d]["real"]) - np.array(data[d]["sys"]), color='#a56cb6', hatch='xx', label="IO")
    # plot total (real)
    h = plt.bar(np.arange(4)*4+2, data[d]["real"], color='#5FA4D9', hatch='//', label="Total")
    plt.legend()
    plt.savefig('recover_'+d+'.pdf', bbox_inches='tight')