import pandas as pd 
import os

files = os.listdir("newdata/")

regions = set([])

# for i,file in enumerate(files):
# 	df = pd.read_csv("newdata/"+file)
# 	if i == 0:
# 		regions = df[df.columns.values[0]].values
# 	else:
# 		regions = [ j for j in df[df.columns.values[0]].values if j in regions]
# 	if len(regions)<5:
# 		print df[df.columns.values[0]].values
# 		break
for i,file in enumerate(files):
	df = pd.read_csv("newdata/"+file)
	regions = regions.union(set(df[df.columns.values[0]].values)) 
regions =list(regions)
	
print len(regions)