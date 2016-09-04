def bubble_sort(lst):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
                is_sorted = False
    return lst


def find_reads_GC_content(fastq_file_name):
    next_line_is_sequence = False
    reads_GC_content = dict()
    with open(fastq_file_name, 'r') as fastq:
        for line in fastq:
            if next_line_is_sequence:
                GC_content = find_GC_content(line)
                if GC_content not in reads_GC_content:
                    reads_GC_content[GC_content] = 0
                reads_GC_content[GC_content] += 1
                next_line_is_sequence = False
            if line.startswith('@'):
                next_line_is_sequence = True
    return reads_GC_content


def find_GC_content(sequence):
    return round((sequence.count('G') + sequence.count('C'))/len(sequence) * 100)


reads_GC_content = find_reads_GC_content('1.fq')
with open('reads_GC_content', 'w') as file:
    for i in range(100):
        file.write('{0}% - {1} reads \n'.format(i, reads_GC_content.get(i, 0)))



