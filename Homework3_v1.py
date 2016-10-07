# Вам нужно сгенерировать маленький случайный участок генома и сгенерировать из него риды fasta (если хотите, можно и
# fastq). При этом я хочу, чтобы пользователь мог как можно больше настроить, задать параметры генерации через н
# еобязательные аргументы командной строки.
# Вам может понадобиться:
# import random
# random.random() # случайное дробное число от 0 до 1
# random.randint(0, 10) # случайное целое число от 0 до 10 включительно
# random.samle('ACGT', 1) # случайный нуклеотид

import random
import argparse
import itertools
import math
import numpy
import collections


#parser = argparse.ArgumentParser()
# parser.add_argument()


def generate_seq_v1(length, gc_content, nucleotides_probabilities=None):
    seq = ''
    if gc_content:
        gc_content /= 100
        at_content = 1 - gc_content
        nucleotides_probabilities = [at_content / 2, at_content / 2, gc_content / 2, gc_content / 2]
        numpy.random.choice(['A', 'T', 'G', 'C'], p=nucleotides_probabilities)
    for i in range(length):
        seq += numpy.random.choice(['A', 'T', 'G', 'C'], p=nucleotides_probabilities)
    return seq

def generate_seq_v2(length):
    # Для равномерного распределения дает более подходящие значения
    seq = ''
    for i in range(length):
        seq += random.choice('ACGT')
    return seq

def generate_fasta(length=1000, gc_content=None, nucleotides_probabilities=None, output_file_name='output',
                   read_name='No information given'):
    # Что лучше генерировать по одному нуклеотиду - много вызовов функции.
    # Или генерировать всю последовательность - много места занимает
    # TODO: if there is . then don't add ext
    seq = ''
    if gc_content or nucleotides_probabilities:
        seq = generate_seq_v1(length, gc_content, nucleotides_probabilities)
    else:
        seq = generate_seq_v2(length)

    with open(output_file_name + '.fasta', 'w') as file:
        file.write('>' + read_name + '\n')
        for i in range(math.ceil(length / 80)): # Интересный вариант int(21 / 5) + (21 % 5 > 0)
            file.write(seq[80 * i : 80 * (i + 1)] + '\n') # Есть ли в фасте сивол переноса строки? Есть
            # Не очень мб хорошо что в последний раз может быть не 80 символов



generate_fasta()

print('Started')
#print(collections.Counter(generate_seq_v1(100000, 5)))
#print(collections.Counter(generate_seq_v2(100000, 5)))

seq = ''
for i in range(10000):
    seq += numpy.random.choice(['A', 'C', 'G', 'T'], p=[0.1, 0.4, 0.4, 0.1])
for val in collections.Counter(seq).values():
    print (val/10000)