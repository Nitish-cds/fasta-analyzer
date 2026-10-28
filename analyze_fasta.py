import argparse
from collections import Counter

def parse_fasta(filepath):
    """Parses a FASTA file and returns a dictionary of headers and sequences."""
    sequences = {}
    with open(filepath, 'r') as f:
        header = None
        seq_lines = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if header:
                    sequences[header] = "".join(seq_lines)
                header = line[1:]
                seq_lines = []
            elif line:
                seq_lines.append(line)
        if header:
            sequences[header] = "".join(seq_lines)
    return sequences

def analyze_sequences(sequences):
    """Calculates length, GC content, and base composition."""
    results = {}
    for name, seq in sequences.items():
        seq = seq.upper()
        length = len(seq)
        counts = Counter(seq)
        g_count = counts.get('G', 0)
        c_count = counts.get('C', 0)
        
        # Calculate GC percentage safely
        gc_content = ((g_count + c_count) / length * 100) if length > 0 else 0
        
        results[name] = {
            'length': length,
            'gc_content': gc_content,
            'composition': dict(counts)
        }
    return results

def main():
    parser = argparse.ArgumentParser(description="Analyze basic properties of sequences in a FASTA file.")
    parser.add_argument("fasta_file", help="Path to the input FASTA file")
    args = parser.parse_args()

    try:
        sequences = parse_fasta(args.fasta_file)
        if not sequences:
            print("No sequences found. Please check the file format.")
            return

        stats = analyze_sequences(sequences)

        print(f"Analyzed file: {args.fasta_file}")
        print("=" * 40)
        for name, data in stats.items():
            print(f"Sequence ID : {name}")
            print(f"Length      : {data['length']} bp")
            print(f"GC Content  : {data['gc_content']:.2f}%")
            print(f"Composition : {data['composition']}")
            print("-" * 40)

    except FileNotFoundError:
        print(f"Error: The file '{args.fasta_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()