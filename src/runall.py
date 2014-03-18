"""
Script to create all results for camera_analysis project
"""

#from__future__import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import mean_sightings as ms

# ---
#  Declare variables
# ---
data_path = '../data/'
results_path = '../results/'

data_name = 'sightings_tab_lg.csv'
table_name = 'spp_table.csv'
fig_name = 'spp_fig.png'

spp_names = ['Fox', 'Wolf', 'Wolverine']

#  Generate reesutls

spp_recs = []

for spp in spp_names:
	n_records, mu_sightings = ms.get_sightings(data_path + data_name, spp)
	spp_recs.append(n_records)
	
print spp_names
print spp_recs


#  Save table
table = pd.DataFrame({'species': spp_names, 'recs': spp_recs})
table.to_csv(results_path + table_name, index=False)

#  Save figure 
fig, ax = plt.subplots(1,1)
ax.bar([0,1,2], spp_recs)
ax.set_xticklabels(spp_names)
fig.savefig(results_path + fig_name)
