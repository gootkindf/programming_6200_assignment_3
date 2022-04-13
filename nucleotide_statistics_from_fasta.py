"""
file    : nucleotide_statistics_from_fasta.py
history : 20-oct-2021

This program looks through a .txt file containing both sequences and secondary
structures of proteins in FASTA format and outputs a file containing the
accession number and its associated nucleotide statistics.

Sample command for executing the program:

python3 nucleotide_statistics_from_fasta.py -i ss.txt
"""
import sys
import argparse


def main():
    """Business Logic"""
    filenames = get_arg()
    fh_in = get_fh(filenames[0], 'r')
    fh_out = get_fh(filenames[1], 'w')
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_in.close()
    _check_sizes_of_lists(list_headers, list_seqs)
    print_sequence_stats(list_headers, list_seqs, fh_out)
    fh_out.close()


def get_arg():
    """
    This function parses the arguments given in command line and returns a
    filename or help menu
    :return: the infile to be read and the outfile to be printed to
    """
    parser = argparse.ArgumentParser(description='Give the fasta sequence file'
                                                 ' name to do the splitting')
    # Add arguments
    parser.add_argument('-i', '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to the file to open',
                        required=True)
    parser.add_argument('-o', '--outfile',
                        dest='OUTFILE',
                        type=str,
                        help='Path to the file to write',
                        required=True)
    args = parser.parse_args()
    inf = args.INFILE
    outf = args.OUTFILE
    return inf, outf


def get_fh(file=None, r_w=None):
    """
    Function takes two arguments: filename, and rw (the mode in which the file
    should be opened). It returns a usable filehandle.
    :param file: file opened for reading or writing
    :param r_w: mode to open the file in, i.e. read or write
    :return: filehandle
    """
    try:
        f_handle = open(file, r_w)
        return f_handle
    except IOError:
        print(f'IOError: could not open the file: {file} for type {r_w}',
              file=sys.stderr)
        raise
    except ValueError:
        print(f"ValueError: Could not open the file: {file} for type '{r_w}'",
              file=sys.stderr)
        raise


def get_header_and_sequence_lists(fasta_file):
    """
    This function reads through the filehandle and returns a tuple containing
    a pair of lists containing the header names and sequences.
    :param fasta_file: opened FASTA file to be read over
    :return: tuple containing 1) list of headers and, 2) list of sequences
    """
    heads = []
    seqs = []
    sequence = ''
    line_num = 0
    for line in fasta_file.readlines():
        if line.startswith('>') and line_num == 0:
            heads.append(line.rstrip('\n'))
            line_num += 1
        elif line.startswith('>'):
            heads.append(line.rstrip('\n'))
            seqs.append(sequence)
            sequence = ''
            line_num += 1
        else:
            sequence += line.rstrip('\n')
            line_num += 1
    if sequence != '':
        seqs.append(sequence)
    return heads, seqs


def _check_sizes_of_lists(header_list, sequence_list):
    """
    This function looks through the lists of headers and sequences obtained in
    the get_header_and_sequence_lists() function and ensures they are of the
    same length.
    :param header_list: The list of headers in the original file
    :param sequence_list: The list of sequences in the original file
    :return: Returns true if the lists are of the same length
    """
    if len(header_list) != len(sequence_list):
        sys.exit("The size of your sequences and header lists is different\n"
                 "Are you sure the FASTA is in the correct format")
    else:
        return True


def print_sequence_stats(head_list, seq_list, out_file):
    """
    This function takes the lists of headers and sequences and writes them to
    the outfile specified in the command line.
    :param head_list: The list of headers gathered from the original file
    :param seq_list: The list of sequences gathered from the original file
    :param out_file: The file to which the headers and sequence statistics are
    written
    :return:
    """
    out_file.write("Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%"
                   "\n")
    for num, head in enumerate(head_list):
        seq = seq_list[num]
        accession_string = _get_accession(head)
        a_nt = _get_nt_occurrence('A', seq)
        g_nt = _get_nt_occurrence('G', seq)
        c_nt = _get_nt_occurrence('C', seq)
        t_nt = _get_nt_occurrence('T', seq)
        n_nt = _get_nt_occurrence('N', seq)
        gc_content = (g_nt + c_nt) / len(seq) * 100
        out = f'{num+1}\t{accession_string}\t{a_nt}\t{g_nt}\t{c_nt}\t' \
              f'{t_nt}\t{n_nt}\t{len(seq)}\t{round(gc_content, 1)}\n'
        out_file.write(out)


def _get_nt_occurrence(nuc, seq):
    """
    This function takes two arguments: a nucleotide to get statistics on and a
    sequence to look in. It also checks to see if the nucleotide being checked
    for is valid
    :param nuc: The nucleotide being looked for
    :param seq: The sequence being analyzed
    :return: The number of occurrences of the nucleotide in the sequence
    """
    if nuc not in ['A', 'C', 'G', 'T', 'N']:
        sys.exit('Did not code this condition')
    nt_count = seq.count(nuc)
    return nt_count


def _get_accession(head_to_seq):
    """
    This function looks through the figures given in sequence headers and
    returns the accession number.
    :param head_to_seq: The header of the sequence of interest
    :return: Accession number
    """
    index1 = head_to_seq.index(">", 0)
    index2 = head_to_seq.index(" ", 0)
    acc = head_to_seq[index1 + 1:index2]
    return acc


if __name__ == "__main__":
    main()
