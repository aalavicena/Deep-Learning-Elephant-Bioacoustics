#!/usr/bin/env python
# coding: utf-8

# In[1]:


# --- DATASET CHOPPING CODE --- #
# --- SEPARATE CLASSES IN THE MAIN DATASET BEFORE RUNNING THIS CODE ---#

import pandas as pd
import os

# Read metadata for positive class
os.chdir('/mnt/batch/tasks/shared/LS_root/mounts/clusters/hgyna1/code/Users/hgyna1/data')
df = pd.read_csv('metadata1.csv')
df.head()

# randomly sample the files
df=df.sample(n=150) # adjust number of files accordingly

print(df)
df.to_csv('D4new_1.csv')


# In[2]:


# Read metadata for negative class
os.chdir('/mnt/batch/tasks/shared/LS_root/mounts/clusters/hgyna1/code/Users/hgyna1/data')
df = pd.read_csv('metadata0.csv')
df.head()

# randomly sample the files
df=df.sample(n=150) # adjust number of files accordingly

#  Save the chopped dataset
print(df)
df.to_csv('D4new_0.csv')


# In[6]:


import pandas as pd
import os
os.chdir('/mnt/batch/tasks/shared/LS_root/mounts/clusters/hgyna1/code/Users/hgyna1/data')

#c combine positive and negative classes
df = pd.concat(
    map(pd.read_csv, ['D4New_0.csv', 'D4New_1.csv']), ignore_index=True)

# save final dataset
print(df)
df.to_csv('D4new.csv', index=False)


# In[3]:


# Split dataset to train and test sets
import pandas as pd
import numpy as np
import os

os.chdir('/mnt/batch/tasks/shared/LS_root/mounts/clusters/hgyna1/code/Users/hgyna1/data')
df = pd.read_csv('D4new.csv')
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.8

train = df[msk]
test = df[~msk]

train.to_csv('D4_train.csv', index=False)
test.to_csv('D4_test.csv', index=False)

