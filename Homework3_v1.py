import argparse
import math
import random

import numpy


def btw_n_and_m(n, m, k):
    k = int(k)
    if k < n or k > m:
        msg = '{} is not from {} to {}'.format(k, n, m)
        raise argparse.ArgumentTypeError(msg)
    return k


def gc_content_restriction(k):
    return btw_n_and_m(4, 90, k)


def generate_genome_v1(size, gc_content, nucleotides_probabilities=None):
    '''
    generate sequence with known gc content or known nucleotides probabilities
    :param size:
    :param gc_content:
    :param nucleotides_probabilities:
    :return: string sequence
    '''
    genome = ''
    if gc_content:
        gc_content /= 100
        at_content = 1 - gc_content
        nucleotides_probabilities = [at_content / 2, at_content / 2, gc_content / 2, gc_content / 2]
        numpy.random.choice(['A', 'T', 'G', 'C'], p=nucleotides_probabilities)
    else:
        nucleotides_probabilities = [el/100 for el in nucleotides_probabilities ]
    for i in range(size):
        genome += numpy.random.choice(['A', 'T', 'G', 'C'], p=nucleotides_probabilities)
    return genome


def generate_genome_v2(size):
    '''
    generate sequence with even distribution of nucleotides
    :param size:
    :return: string sequence
    '''
    # Для равномерного распределения дает более подходящие значения
    genome = ''
    for i in range(size):
        genome += random.choice('ACGT')
    return genome


def generate_genome_wrapper(size, gc_content=None, nucleotides_probabilities=None):

    if gc_content or nucleotides_probabilities:
        genome = generate_genome_v1(size, gc_content, nucleotides_probabilities)
    else:
        genome = generate_genome_v2(size)
    return genome


def generate_reads_from_genome(genome, reads_number, reads_length):
    #TODO add coverage?
    reads =[]
    step = max((len(genome) - reads_length) // reads_number, 1)
    n = 0
    for i in range(reads_number):
        start_pos = n * step
        end_pos = n * step + reads_length
        if end_pos >=len(genome):
            reads.append(genome[-reads_length:])
            n = 0
        else:
            reads.append(genome[start_pos: end_pos])
            n += 1
    random.shuffle(reads)
    return reads


def generate_fasta(reads_number, reads_length, genom_size, output_file_name, gc_content=None, nucleotides_probabilities=None):
    # Что лучше генерировать по одному нуклеотиду - много вызовов функции.
    # Или генерировать всю последовательность - много места занимает
    # TODO: if there is . then don't add ext
    output_file_name = output_file_name.split('.')[0] + '.fasta'
    genome = generate_genome_wrapper(genom_size, gc_content, nucleotides_probabilities)
    print(genome)

    with open(output_file_name, 'w') as file:
        for number, read in enumerate(generate_reads_from_genome(genome, reads_number, reads_length)):
            file.write('> noname read {}\n'.format(number + 1))
            print(read)
            for i in range(math.ceil(reads_length / 80)): # Интересный вариант int(21 / 5) + (21 % 5 > 0)
                file.write(read[80 * i : 80 * (i + 1)] + '\n') # Есть ли в фасте сивол переноса строки? Есть
            # Не очень мб хорошо что в последний раз может быть не 80 символов
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--reads_length', type=int, help='Length of the read to generate',
                    default=50)
    parser.add_argument('--gc_content', type=gc_content_restriction, help='Desired GC content. From 4 to 90')
    parser.add_argument('-o', '--output', type=str,
                    dest='output_file_name',
                    default='output',
                    help='Name of the output file without extention. All chars after . will be discarded')
    parser.add_argument('--nucleotides_prob', nargs='+', type=int,
                    dest='nucleotides_probabilities',
                    default=argparse.SUPPRESS,
                    help='Desired nucleotides probabilities in next order: A T G C')
    parser.add_argument('-s', '--genom_size', type=int,
                    default=100000,
                    help='Size of the genome to generate in bp')
    parser.add_argument('-n', '--reads_number', type=int,
                    default=10, help='number of reads to generate')

    args = vars(parser.parse_args())
    print(args)
    generate_fasta(**args)

