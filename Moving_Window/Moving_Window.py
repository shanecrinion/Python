#!/usr/bin/env python
# coding: utf-8

# In[ ]:


data_file =  "chrM.fa"

# concatenate the data
with open(data_file) as DNA_raw:
    next(DNA_raw)
    # clean up: use upper() to remove lower case
    DNA_raw = DNA_raw.read().upper()
    # clean up: use isalnum() to test if all are alpha-numeric on raw data    
    print(DNA_raw.isalnum())
    # clean up: extract only those that are ATGC 
    dna = DNA_raw
    my_ATGC = re.split(r"[^ATGC]", dna) # limit the sequence to only ATGCs 
    conc_DNA = ''.join(map(str, my_ATGC))
    DNA_list = list(conc_DNA)
    print(conc_DNA.isalnum())
    
    # reverse complement: create a fucntion to generate the reverse complement
    def reverse_complement(conc_DNA):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} # create dictionary stating the complement
        rc_DNA = ''.join([complement[base] for base in conc_DNA[::-1]]) # join all the reverse together
        return(rc_DNA) 
   # make a string of the reversed bases
    rev = reverse_complement(conc_DNA)
    rev = ''.join(map(str, rev))

    
    #create a start time 
    start = 0    

    # create a window for all the sequences within the range to limit to this size being examined
    palindromes = []
    independantcount=[]
    for window in range(6,21):
        # go only up to the length of the sequece
        for i in range(0,len(conc_DNA)):
            windowseq=conc_DNA[i:window+i] #increase window increment in each instance
            if windowseq==reverse_complement(windowseq): # limit the rev comp to only the window length
                start = start + 1 # increase start 
        independantcount.append("Window:"+str(window)+" Count:"+str(start))
        start=0
    print(independantcount) #print independantcount as the number of palindromes.
    
# import to make a dataframe
import numpy as np
import pandas as pd

# make empty lists for window and count
windowList = []
countList = []

# split the generated list from the palindrome counter above by the space
for i in independantcount:
    countList.append(i.split(' ')[1]) # use the index 0 value as this is the count subset
for i in independantcount:
    windowList.append(i.split(' ')[0]) # use the index 1 value as this the window subset

# split the new list again by removing the count/list
countListvalues = []
windowListvalues = []

for i in countList:
    countListvalues.append(i.split('Count:')[1]) # use the index 1 value as this is the actual value
for i in windowList:
    windowListvalues.append(i.split('Window:')[1]) # use the index 1 value as this is the actual value


# create a data frame which will appear as a table!                       
data = pd.DataFrame(
    {
     'Window': windowListvalues,
     'Count': countListvalues
    })
data

