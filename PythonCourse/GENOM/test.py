from graph_tool.all import *

import PythonCourse.GENOM.overlap_assembler as ov

g = Graph()


with open('test.dna', 'r') as f:
    reads = [line.strip() for line in f]
#    dedup_reads = set(reads)
#    print(len(reads))
    #print(len(dedup_reads))
    # multi_reads = [ass.gen_kmers_from_reads(reads, i) for i in range(8, 100, 15)]
#genome = 'ACTAGCTCGGCTAGCGCTAGCGCTAGC'
#reads = ass.gen_kmer_from_read(genome, 10)
#print(ass.de_bruijn_ize_2(reads, 60))
#
#
# import random

#genome = h3.Genome(size=200)
#seq = genome.get_sequence()
#reads2 = h3.generate_random_reads_from_genome(seq, 100, 20)
#graph = ass.de_bruijn_ize_3(reads, 30)
#print(ass.eulerian_path2(graph))
#print(ass.reconstr_from_reads_2())

# ############################################
#graph, start = ov.overlap_graph(reads, 50)
#for key in graph:
##    v1 = g.add_vertex()
#    v2 = g.add_vertex()
    #g.add_edge(v1, v2)
assemble = ov.assemble(*ov.overlap_graph(reads, 50))
# print(seq)
#for read in reads:
#    if read not in assemble:
#       raise
# print(assemble)
#
#
# assemble = ov.assemble(*ov.overlap_graph(reads, 50))
# #print(seq)
#
# print(len(assemble))
# # #print(seq)
# # reads_set = set(reads)
# # for read in reads_set:
# #     if read not in assemble:
# #         print('Fuck')
# #
# # #print(len(assemble))
#
# # kmers = [i for i in range(8, 100, 15)]
# # multi_genomes = [ass.reconstr_from_reads(reads_) for reads_ in multi_reads]
# # for genome, kmer in zip(multi_genomes, kmers):
#     print('kmer -',kmer, len(genome))
