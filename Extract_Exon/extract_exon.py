#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. extract the exon sequences.
# open my genomic data
# open my exon locations
# skip the location in 1st line (states it's mRNA)
exon1 = 'exons.txt'
sequence1 = 'genomic_RNA.fa'

def extract_exon(exon,sequence):
    with open(sequence) as genomic_rna, open(exon) as exon_locations:
            next(genomic_rna)

# 2. concatenate the data.
            coding_sequence = "" #
            for line1 in genomic_rna:
                for i in exon_locations:
                    positions = i.split(',') 
                    exon_start = int(positions[0]) 
                    exon_stop = int(positions[1]) 
                    exon = line1[exon_start:exon_stop] 
                    coding_sequence = coding_sequence + exon 
                print('The spliced mRNA sequence is:\n', coding_sequence)
                
# 3. write the info to a new FASTA file.
                output = open("genomic_mRNA.fa","w")
                output.write('>genomic_mRNA\n')
                output.write(coding_sequence)
                output.close()
                
extract_exon(exon1,sequence1)
