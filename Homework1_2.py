
def find_subseq_with_highest_quality(seq, quality_seq, quality_dict):
    """Return subsequence with the best quality or None if there is no subsequence with quality greater than 0

        seq - some sequence (str)
        quality_seq - sequence containing quality(in char representation) of each symbol from seq(str)
        quality_dict - dictionary, which keys are all symbols that may be found in quality_seq and values are int
            representations of quality (dict)
    """
    translated_quality_seq = [quality_dict[i] for i in quality_seq]
    highest_quality = 0
    is_started = False
    for i, e in enumerate(translated_quality_seq):
        if (e > 0) and not is_started:
            quality = 0
            start_pos = i
            is_started = True
        if is_started:
            quality += e
            if quality >= highest_quality:
                highest_quality = quality
                highest_quality_subseq_start_pos = start_pos
                highest_quality_subseq_end_pos = i
            elif quality < 0:
                is_started = False

    if highest_quality == 0:
        return None
    else:
        return seq[highest_quality_subseq_start_pos: highest_quality_subseq_end_pos + 1]


def find_highest_quality_subsequences_of_reads(fastq_file_name):
    subsequences_with_highest_quality = []
    quality_chars = '''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
    quality_dict = {i: j for i, j in zip(quality_chars, range(-34, 60))}
    with open(fastq_file_name, 'r') as fastq:
        for i, line in enumerate(fastq):
            if i % 4 == 1:  # since every fourth string starting from the first is a coding sequence
                seq = line.strip()
                #print(seq)
            elif i % 4 == 3:
                quality_seq = line.strip()
                #print(quality_seq)
                subsequences_with_highest_quality.append(find_subseq_with_highest_quality(seq, quality_seq, quality_dict))
    return subsequences_with_highest_quality



reads_highest_quality_subsequences = find_highest_quality_subsequences_of_reads('1.fq')
with open('reads_highest_quality_subsequences', 'w') as file:
    for i, e in enumerate(reads_highest_quality_subsequences):
        file.write('{0} - {1} \n'.format(i, e))




