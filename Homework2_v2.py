import argparse
import sys
from Homework2 import find_gc_content


def fastq_to_csv(inp_file, outp_file, lower_gc_content_bound=None, upper_gc_content_bound=None, gc_content_values=None):
    '''

    :param inp:
    :param outp:
    :param lower_gc_content_bound:
    :param upper_gc_content_bound:
    :param gc_content_values:
    :return:
    '''
    #print(lower_gc_content_bound, upper_gc_content_bound, gc_content_values)

    if gc_content_values:
        for line in inp_file:
            name = line.strip()
            seq = next(inp_file).strip()
            next(inp_file)
            next(inp_file)
            gc_content = find_gc_content(seq)
            if gc_content in gc_content_values:
                outp_file.write('{}\t{}\t{}\n'.format(name, len(seq), gc_content))
    else:
        for line in inp_file:
            name = line.strip()
            seq = next(inp_file).strip()
            next(inp_file)
            next(inp_file)
            gc_content = find_gc_content(seq)
            if lower_gc_content_bound <= gc_content <= upper_gc_content_bound:
                outp_file.write('{}\t{}\t{}\n'.format(name, len(seq), gc_content))
    outp_file.close()
    inp_file.close()


def btw_0_and_100(n):
    n = int(n)
    if n < 0 or n > 100:
        msg = '{} is not from 0 to 100'.format(n)
        raise argparse.ArgumentTypeError(msg)
    return n


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-i', type=argparse.FileType('r'), required=True,  # Required options are generally
                        # considered bad form because users expect options to be optional, and thus they should be
                        # avoided when possible
                        dest='inp_file',
                        help='fastq file name')
    # The parse_args() method by default allows long options to be abbreviated to a prefix,
    #  if the abbreviation is unambiguous (the prefix matches a unique option):
    parser.add_argument('-o', type=argparse.FileType('w'), required=True,
                        dest='outp_file',
                        help='csv file name')
    parser.add_argument('-a', default=55, type=btw_0_and_100,
                        dest='lower_gc_content_bound',
                        help='''gc content\'s lower bound. seqs which gc content is not lower than this will be included in
                             csv file. default: %(default)s'''
                        )
    parser.add_argument('-b', default=75, type=btw_0_and_100,
                        dest='upper_gc_content_bound',
                        help='''gc content\'s upper bound. seqs which gc content is not greater than this will be included in
                            csv file. default: %(default)s'''
                        )
    parser.add_argument('-g', nargs='+', default=argparse.SUPPRESS,
                        dest='gc_content_values',
                        type=int,
                        help='list of gc content values. seq with such gc contents will be included in csv file')

    #args = parser.parse_args(['-i','inp.fq','-o','outp2.csv','-a','30', '-b','50', '-g','50','45','35'])
    #print(args)
    args = parser.parse_args(sys.argv[1:])
    args = vars(args)
    fastq_to_csv(**args)
