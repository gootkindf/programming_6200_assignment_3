"""
file    : pdb_fasta_splitter.py
history : 19-oct-2021

This program looks through a .txt file containing both sequences and secondary
structures of proteins in FASTA format and outputs files containing the IDs of
both the sequences and secondary structures. It also prints the total number
of IDs found.

Sample command for executing the program:

python3 pdb_fasta_splitter.py -i ss.txt
"""
import sys
import argparse


def main():
    """Business Logic"""
    filename = get_arg()
    fh_in = get_fh(filename, 'r')
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_in.close()
    _check_sizes_of_lists(list_headers, list_seqs)
    fh_out_pr = get_fh('pdb_protein.fasta', 'w')
    fh_out_ss = get_fh('pdb_ss.fasta', 'w')
    pr_count = 0
    ss_count = 0
    for num, head in enumerate(list_headers):
        if 'sequence' in head:
            entry = f'{head}\n{list_seqs[num]}\n'
#            fh_out_pr.write(head)
#            fh_out_pr.write(list_seqs[num])
            fh_out_pr.write(entry)
            pr_count += 1
        else:
            entry = f'{head}\n{list_seqs[num]}\n'
#            fh_out_ss.write(head)
#            fh_out_ss.write(list_seqs[num])
            fh_out_ss.write(entry)
            ss_count += 1
    fh_out_pr.close()
    fh_out_ss.close()
    print("Found {} protein sequences\nFound {} ss sequences"
          .format(pr_count, ss_count))


def get_arg():
    """
    This function parses the arguments given in command line and returns a
    filename or help menu
    filehandle  : get_f
    :return:
    """
    parser = argparse.ArgumentParser(description='Give the fasta sequence file'
                                                 'name to do the splitting')
    # Add arguments
    parser.add_argument('-i', '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to the file to open',
                        required=True)
    args = parser.parse_args()
    inf = args.INFILE
    return inf


def get_fh(file=None, r_w=None):
    """
    Function takes two arguments: filename, and rw (the mode in which the file
    should be opened).
    It returns a usable filehandle
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
    :param: opened FASTA file to be read over
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


if __name__ == "__main__":
    main()
