# FASTA Sequence Analyzer

A lightweight, zero-dependency Python script to read a public sequence file (FASTA format) and report basic properties of the sequences.

## Features
- **Custom FASTA Parser:** Reads standard FASTA formatting without requiring external libraries like Biopython.
- **Metrics Reported:** Sequence length, GC content (percentage), and overall nucleotide composition.
- **Portability:** Runs on any valid FASTA file of the same format.

## How to Run

**Prerequisites:** Python 3.x

Run the script from your terminal, passing the path to the FASTA file as an argument:

```bash
python analyze_fasta.py example.fasta