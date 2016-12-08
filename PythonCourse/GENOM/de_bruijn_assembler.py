import PythonCourse.GENOM.graph as g


def gen_kmer_from_read(read, k):
    return [read[i:i+k] for i in range(len(read)-k+1)]


def gen_kmers_from_reads(reads, k):
    kmers = []
    for read in reads:
        kmers.extend(gen_kmer_from_read(read, k))
    return kmers


def de_bruijn_ize(reads, k):
    graph = g.DeBruijnGraph(k)
    for read in reads:
        for i in range(len(read) - k):
            graph.add_edge(read[i: i+k], read[i+1: i+k+1])
    print('Graph is built')
    return graph
