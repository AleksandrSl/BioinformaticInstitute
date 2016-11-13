import collections

def find_reads_GC_content(fastq_file_name):
    next_line_is_sequence = False
    reads_GC_content = collections.defaultdict(int)  # Cool stuff
    with open(fastq_file_name, 'r') as fastq:
        for line in fastq:
            if next_line_is_sequence and not line.startswith('@'):
                GC_content = find_GC_content(line)
                reads_GC_content[GC_content] += 1
                next_line_is_sequence = False
            if line.startswith('@'):
                next_line_is_sequence = True
    return reads_GC_content

def find_reads_GC_content_v2(fastq_file_name):
    reads_GC_content = collections.defaultdict(int)  # Cool stuff
    with open(fastq_file_name, 'r') as fastq:
        for i, line in enumerate(fastq):
            if i % 4 == 1:   # since every fourth string starting from the first is a coding sequence
                GC_content = find_GC_content(line)
                reads_GC_content[GC_content] += 1
    return reads_GC_content


def find_GC_content(sequence):
    return round((sequence.count('G') + sequence.count('C')) / len(sequence) * 100)


reads_GC_content = find_reads_GC_content('1.fq')
with open('reads_GC_content', 'w') as file:
    for i in range(100):
        file.write('{0}% - {1} reads \n'.format(i, reads_GC_content.get(i, 0)))

reads_GC_content = find_reads_GC_content_v2('1.fq')
with open('reads_GC_content_v2', 'w') as file:
    for i in range(100):
        file.write('{0}% - {1} reads \n'.format(i, reads_GC_content.get(i, 0)))

with open('reads_GC_content', 'r') as file1, open('reads_GC_content_v2', 'r') as file2:
    count = 0
    for line1, line2 in zip(file1, file2):
        if line1 == line2:
            count += 1
        else:
            count -= 1
    print(count)


