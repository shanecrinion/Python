**CTCF-finder** 

- Cleans DNA data by changing to uppercase
- Uses regular expression to search for any CTCF binding site
- Used regular expression to find all CTCF binding sites
- Print each binding site and their start/stop location

**Extract_Exon**

- Cleans exon data by splitting coding sequence
- Prints each spliced mRNA sequence
- Writes the coding region and header into FASTA file.

**Moving_Window**

- Clean DNA data with upper case and confirmation of alpha-numeric format
- Split to contain only nucleotides
- Create "reverse_complement" function 
- Use a for loop to identify the number of palindromes in the DNA sequence
- Use numpy and pandas to create a table containing a palindrome counter for each window size

**BioPython-GenBank-DiseaseVariants.ipynb**

- Download SeqRecord data using Entrez data parser
- Extract coding sequence and concatenate exons
- Translate the sequence and compare to GenBank amino acid sequence
- Determine suitable restriction enzymes using the identified sequence for disease variant testing
- Test restriction sites in the normal and mutated sequences.
