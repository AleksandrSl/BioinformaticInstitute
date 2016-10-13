import argparse
import math
import random

import numpy


# class genome(object):
#     size = None

def generate_genome_v1(size, gc_content=None, nucleotides_probabilities=None):
    '''
    generate sequence with known gc content or known nucleotides probabilities
    :param size:
    :param gc_content:
    :param nucleotides_probabilities:
    :return: string sequence
    '''
    genome = '' # [] try
    if gc_content:
        gc_content /= 100
        at_content = 1 - gc_content
        nucleotides_probabilities = [at_content / 2, at_content / 2, gc_content / 2, gc_content / 2]

        numpy.random.choice(['A', 'T', 'G', 'C'], p=nucleotides_probabilities)
    else:
        nucleotides_probabilities = [el/100 for el in nucleotides_probabilities] # In python2 this will not work
    for i in range(size):
        genome += numpy.random.choice(['A', 'T', 'G', 'C'], p=nucleotides_probabilities)
    return genome


def generate_genome_v2(size):
    '''
    generate sequence with even distribution of nucleotides
    :param size:
    :return: string sequence
    '''
    # Both version of generate_genome works well
    genome = ''
    for i in range(size):
        genome += random.choice('ACGT')
    return genome



def btw_n_and_m(n, m, k):
    k = int(k)
    if k < n or k > m:
        msg = '{} is not from {} to {}'.format(k, n, m)
        raise argparse.ArgumentTypeError(msg)
    return k


def gc_content_restriction(k):
    return btw_n_and_m(4, 90, k)




# import collections # Test to random functions, whether they have similar "error rate"
# def chisq(size):
#     g1 = generate_genome_v2(size)
#     g2 = generate_genome_v1(size, nucleotides_probabilities=[25, 25, 25, 25])
#     gd1 = collections.Counter(g1)
#     gd2 = collections.Counter(g2)
#
#     chi1 = 0
#     for i in gd1.values():
#         chi1 += (i - size/4)**2/(size/4)
#
#     chi2 = 0
#     for i in gd2.values():
#         chi2 += (i - size/4)**2/(size/4)
#     return (chi1, chi2)
#
# chi_m1 = 0
# chi_m2 = 0
# for i in range(100000):
#     t1, t2 = chisq(1000)
#     chi_m1 += t1
#     chi_m2 += t2
# print(chi_m1/100000, chi_m2/100000)

def generate_genome_wrapper(size, gc_content=None, nucleotides_probabilities=None):

    if gc_content or nucleotides_probabilities:
        genome = generate_genome_v1(size, gc_content, nucleotides_probabilities)
    else:
        genome = generate_genome_v2(size)
    return genome


def generate_reads_from_genome(genome, reads_number, reads_length):
    #TODO add coverage?
    reads = []
    step = max((len(genome) - reads_length) // reads_number, 1)
    n = 0
    for i in range(reads_number):
        start_pos = n * step
        end_pos = n * step + reads_length
        if end_pos >= len(genome):
            reads.append(genome[-reads_length:])
            n = 0
        else:
            reads.append(genome[start_pos: end_pos])
            n += 1
    random.shuffle(reads)
    return reads

def generate_random_reads_from_genome(genome, reads_number, reads_length):
    reads = []
    genome_len = len(genome)
    for _ in range(reads_number):
        start_pos = random.randint(0, genome_len - reads_length)
        end_pos = start_pos + reads_length
        reads.append(genome[start_pos: end_pos])
    return reads

def generate_fasta(reads_number, reads_length, func, genom_size, output_file_name, gc_content=None, nucleotides_probabilities=None):
    func_dict = {1: generate_reads_from_genome, 2: generate_random_reads_from_genome}
    func = func_dict[func]
    # TODO: if there is . then don't add ext
    output_file_name = output_file_name.split('.')[0] + '.fasta'
    genome = generate_genome_wrapper(genom_size, gc_content, nucleotides_probabilities)
    # print(genome)

    with open(output_file_name, 'w') as file:
        for number, read in enumerate(func(genome, reads_number, reads_length)):
            file.write('> noname read {}\n'.format(number + 1))
            # print(read)
            for i in range(math.ceil(reads_length / 80)): # Interesting int(21 / 5) + (21 % 5 > 0)
                file.write(read[80 * i : 80 * (i + 1)] + '\n')
    return None

# def is_sum_equal_100(numbers):  # Doesn't work, because in this case function get only one argument
#     numbers = [int(el) for el in numbers]
#     print(numbers)
#     if sum(numbers) != 100:
#         raise argparse.ArgumentError('Sum of the probabilities should be equal 100')
#     return numbers


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--reads_length', type=int, help='Length of the read to generate',
                    default=50)
    parser.add_argument('--gc_content', type=gc_content_restriction, help='Desired GC content. From 4 to 90')
    parser.add_argument('-o', '--output', type=str,
                    dest='output_file_name',
                    default='output2',
                    help='Name of the output file without extention. All chars after . will be discarded')
    parser.add_argument('--nucleotides_prob', nargs=4, type=int,
                    dest='nucleotides_probabilities',
                    default=argparse.SUPPRESS,
                    help='Desired nucleotides probabilities in next order: A T G C')
    parser.add_argument('-s', '--genom_size', type=int,
                    default=100000,
                    help='Size of the genome to generate in bp')
    parser.add_argument('-n', '--reads_number', type=int,
                    default=10, help='number of reads to generate')
    parser.add_argument('-f','--function', type=int, default=1, dest='func',
                        help='Method by which the reads will be generated: 1 - max coverage, 2 - random reads')

    args = vars(parser.parse_args())
    #print(args)
    generate_fasta(**args)

