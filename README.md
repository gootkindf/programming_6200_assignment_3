# Assignment 3: pdb_fasta_splitter.py & nucleotide_statistics_from_fasta.py

This assignment contains two scripts: pdb_fasta_splitter.py, separates a FASTA
file into protein and ss fasta files, and nucleotide_statistics_from_fasta.py:
reads a FASTA file and outputs a data file containing stats about the genes

## Description

These programs can be called provided they have the correct arguments given.
pdb_fasta_splitter.py requires an input argument, while nucleotide_statistics_
from_fasta.py needs an input and output argument.

Both of these programs loop through .txt files containing info in a FASTA
format. pdb_fasta_splitter.py separates out the header information from the
files into two fasta files, while nucleotide_statistics_from_fasta.py prints a
.txt file containing stats about the proteins.

## Getting Started

### Dependencies

* Python 3

### Executing program

* Call pdb_fasta_splitter.py with an input argument
* Call nucleotide_statistics_from_fasta with an input and output argument
```
python3 pdb_fasta_splitter.py -i myfile.txt
python3 nucleotide_statistics_from_fasta.py -i myfile.txt -o output.fasta
```

## Help

If you run into any problems, run the help command
```
python3 pdb_fasta_splitter.py -h
python3 nucleotide_statistics_from_fasta.py -h
```

## Authors
Fredrick Gootkind

## Version History

* 0.1
    * Initial Release

## Acknowledgments

Inspiration, code snippets, etc.
https://gist.githubusercontent.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc/raw/d59043abbb123089ad6602aba571121b71d91d7f/README-Template.md_