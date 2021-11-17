import json
from os import linesep 
import pandas as pd
import numpy as np
import json 
from missingpy import MissForest
from os import walk

metaPath='./metadata'
_, _, files = next(walk(metaPath))
print(files)

# for i in range(0,len(files_names)):
#     print(files_names[i])
#     df = pd.read_json(metaPath+files_names[i], nrows=10000,lines =True)
    
#     out1 = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')

#     path1 = "./D10k/"+files_names[i]+ "10k.json"
   
    
#     with open(path1, 'w') as f:
#         f.write(out1)

