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
import numpy
import collections


#parser = argparse.ArgumentParser()
# parser.add_argument()


def generate_seq_v1(length, gc_content, nucleotides_probabilities=None):
    seq = ''
    if nucleotides_probabilities:
        print(nucleotides_probabilities)
    for i in range(length):
        seq += numpy.random.choice(['A', 'C', 'G', 'T'], p=nucleotides_probabilities)
    return seq

def generate_seq_v2(length, gc_content):
    # Для равномерного распределения дает более подходящие значения
    seq = ''
    for i in range(length):
        seq += random.choice('ACGT')
    return seq


print('Started')
print(collections.Counter(generate_seq_v1(100000, 5)))
print(collections.Counter(generate_seq_v2(100000, 5)))

seq = ''
for i in range(10000):
    seq += numpy.random.choice(['A', 'C', 'G', 'T'], p=[0.1, 0.4, 0.4, 0.1])
for val in collections.Counter(seq).values():
    print (val/10000)