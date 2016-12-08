import PythonCourse.GENOM.graph as graph


def find_overlap(a, b, min_overlap):
    start = 0
    while True:
        start = a.find(b[:min_overlap], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1


def assemble_one_sequence(overlap_graph_, start):
    """
    assemble one sequence from start read, presume that all reads in overlap graph present only one time
    :param overlap_graph_:
    :param start:
    :return: assembled sequence, str
    """
    print('Starts assembling')
    seq = []
    pos = 0
    next_ = overlap_graph_.vertices[start]
    print(next_)
    while next_ is not None:
        seq.append(next_.value[pos:])
        next_, pos = next_.pop_out_edge()
    return ''.join(seq)


def assemble_circular_chr(overlap_graph_):
    print('Starts assembling')
    _, start = overlap_graph_.vertices.popitem()
    stop = start.index
    next_, pos = start.pop_out_edge()
    seq = [start.value]
    while next_.index != stop:
        seq.append(next_.value[pos:])
        next_, pos = next_.pop_out_edge()
    print('Assembling is done')
    return ''.join(seq)[:-pos]


def assemble_one_sequence_retaining_reads(overlap_graph_, start, n):
    """
    assemble one sequence from start read, presume that all reads in overlap graph present only one time
    :param overlap_graph_:
    :param start:
    :param n:
    :return: assembled sequence, str
    """
    print('Starting assembling')
    seq = []
    pos = 0
    with open('chr' + str(n), 'w') as out:
        out.write('>chr' + str(n) + '\n')
        next_ = overlap_graph_.vertices[start]
        print(next_)
        while next_ is not None:
            seq.append(next_.value[pos:])
            out.write(next_.value + '\n')
            next_, pos = next_.pop_out_edge()
    return ''.join(seq)


def overlap_graph(reads, min_overlap):
    graph_ = graph.WeightedGraph()
    start = set(reads)
    for read1 in reads:
        for read2 in reads:
            if read1 == read2:
                continue
            overlap = find_overlap(read1, read2, min_overlap)
            if overlap != 0:
                graph_.add_edge(read1, read2, overlap)
                if read2 in start:
                    start.remove(read2)
    graph_.sort_out_by_weight()
    print('Graph is built')
    return graph_, start


def assemble(overlap_graph_, starts) -> list:
    fragments = []
    i = 1
    for start in starts:
        fragments.append(assemble_one_sequence_retaining_reads(overlap_graph_, start, i))
        i += 1
    return fragments

if __name__ == '__main__':
    with open('test.dna', 'r') as f:
        reads = [line.strip() for line in f]
    l = 0
    for read in reads:
        l += len(read)
    print(l)
    genome = assemble(*overlap_graph(reads, 50))
    print(len(''.join(genome)))
