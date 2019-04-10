#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### 1. open the file as new variable DNA_seq

# open the file as new variable DNA_seq
with open('intron.txt','r') as raw_data:
    DNA_seq = raw_data.read()
    print(DNA_seq)

### 2. determine if a CTCF binding site is present

DNA_seq = DNA_seq.upper()
import re
# compile all the possible sequences
CTCF_bs = re.compile(r"CC...AG..GG")
# search for all the possible sequences
if re.search(CTCF_bs,DNA_seq):
    print('CTCF binding site found!')
else: 
    print('CTCF binding site not found!')

### 3. determines if there is more than one.

# use the regular expression function to find all.
CTCF_all = re.findall('CC...AG..GG',DNA_seq)
CTCF_all
# use the regular expression function to find all.
if len(CTCF_all) >= 1:
print('There are one or more CTCF binding site in the sequence.')
# changed the above to 1 or more because there is only 1 so I didn't get any results

### 4. prints the actual matching sequence(s) that occur in the original DNA sequence.

# print all from the 'list' of CTCF binding sites
print(CTCF_all)
CTCF_all = CTCF_all[0] # pull the 1st as it is the only binding site.

### 5. prints the start/stop location of any detected CTCF binding sites.

CTCF_start = DNA_seq.index(CTCF_all) # use the index the first sequence
CTCF_pos = [CTCF_start,CTCF_start + len(CTCF_all)] # add the length of the binding si
print(CTCF_pos)

