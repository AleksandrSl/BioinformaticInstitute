import time
from functools import wraps

import PythonCourse.GENOM.de_bruijn_assembler as db
import PythonCourse.GENOM.overlap_assembler as ov


def timethis(func):
    """
    Decorator that reports the execution time
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('function:{} runned {:f} seconds'.format(func.__name__, end-start))
        return result
    return wrapper


@timethis
def assemble(func):
    for _ in range(1):
        graph_, starts = func(reads, 50)
        start = starts.pop()
        ass = ov.assemble_one_sequence(graph_, start)
        return ass

# with open('test.dna', 'r') as f:
#    reads = [line.strip() for line in f]
#
# graph, _ = ov.overlap_graph(reads, 49)
# print(graph.connected_components())

graph1 = ov.graph.WeightedGraph()
graph1.add_edge(1, 2, 1)
graph1.add_edge(2, 3, 1)
graph1.add_edge(4, 5, 1)
graph1.add_edge(6, 7, 1)
graph1.add_node(100)

assert graph1.connected_components() == 4

inital_seq = '123456783459ABCD'
reads = db.gen_kmer_from_read(inital_seq, 6)
print(reads)
graph2 = db.de_bruijn_ize(reads, 3)
print('Initial graph')
graph2.adjacency_list()
graph2.simplify_de_bruijn()
print('Simplified graph')
graph2.adjacency_list()
graph2.eulerian_path()
print(graph2.eulerian_walk)
print('Reconstructed', graph2.reconstruct_from_eul_walk())
assert graph2.reconstruct_from_eul_walk() == inital_seq

################## Хромосома линейная здесь собирается ###########################
# with open('assembled/chr2', 'r') as fa:
#     reads = [line.strip() for line in fa]
# graph3 = db.de_bruijn_ize(reads, 48)
# # graph3.adjacency_list()
# graph3.simplify_de_bruijn()
# print('Simplified graph')
# graph3.adjacency_list()
# graph3.eulerian_path()
# print('Reconstructed length', len(graph3.reconstruct_from_eul_walk()))

################## Хромосома с повтором здесь собирается ###########################
with open('assembled/chr0', 'r') as fa:
    reads = [line.strip() for line in fa]

graph4, _ = ov.overlap_graph(reads, 48)
graph4.simplify()
graph4.draw('chr0_overlap.png')
graph3 = db.de_bruijn_ize(reads, 48)
graph3.simplify_de_bruijn()
print('Simplified graph')
graph3.draw('chr0_de_bruijn.png')
graph3.adjacency_list()
graph3.eulerian_path()
print('Reconstructed length', len(graph3.reconstruct_from_eul_walk()))


# with open('chr4', 'r') as fa:
#     name = fa.readline()
#     reads = [line.strip() for line in fa]
#
# graph_, starts = ov.overlap_graph(reads, 50)
# start = starts.pop()
# graph_.simplify(start)
# graph_.draw_from_start(start)
# print(graph_.adjacency_list())
# print(graph_.vertices.values())
# assemble = ov.assemble_one_sequence(graph_, start)
# with open('chr4.ass', 'w') as fa:
#     print(len(assemble))
#     fa.write(assemble)

# with open('chr1 + chr3', 'r') as fa:
#     name = fa.readline()
#     reads = [line.strip() for line in fa]
#
# graph_, starts = ov.overlap_graph(reads, 50)
# start = starts.pop()
# graph_.simplify(start)
# graph_.draw_from_start(start)
# print(graph_.adjacency_list())
# print(graph_.vertices.values())
# assemble = ov.assemble_one_sequence(graph_, start)
# print(len(assemble))
#
# with open('shitty.dna', 'w') as fa, open('chr1', 'r') as fa1, open('chr3', 'r') as fa3:
#     fa1.readline()
#     chr1 = [line.strip() for line in fa1]
#     fa3.readline()
#     chr3 = [line.strip() for line in fa3]
#     for read in itertools.chain(chr1, chr3):
#             fa.write(read + '\n')
#
# with open('chr2', 'r') as fa1, open('chr4', 'r') as fa2, open('alien.dna', 'r') as alien,
# open('shitty.dna', 'r') as fa3, open('mysterious.dna', 'w') as fa4:
#     fa1.readline()
#     chr1 = set([line.strip() for line in fa1])
#     fa2.readline()
#     chr0 = set([line.strip() for line in fa2])
#     reads = set([line.strip() for line in alien])
#     chr3 = set([line.strip() for line in fa3])
#     count = 0
#     for read in itertools.chain(chr1, chr0, chr3):
#         if read in reads:
#             reads.remove(read)
#             count += 1
#     for read in reads:
#         fa4.write(read + '\n')
#     print(count)

# with open('shitty.dna') as fa:
#     reads = [read.strip() for read in fa]
#
# graph_, starts = ov.overlap_graph(reads, 43)
# print(starts)
# graph_.draw('shiity.png')
#
# with open('mysterious.dna') as fa:
#     reads = [read.strip() for read in fa]
#
# graph_, starts = ov.overlap_graph(reads, 43)
# graph_.draw('mysterious.png')
# print(starts)

# with open('not_assembled') as fa:
#    reads = [read.strip() for read in fa]
# with open('not_assembled.graph', 'w') as graph_file:
#     from json import dump
# graph_, starts = ov.overlap_graph(reads, 45)
#     dump(graph_, graph_file)

# graph_.draw('not_assembled.png')
# graph_.connected_components()
# read_file = ['chr5', 'chr1', 'chr0', 'chr3']
# for file_name in read_file:
#     with open(file_name, 'r') as fa:
#         reads = [read.strip() for read in fa]
#     graph_, starts = ov.overlap_graph(reads, 45)
#     graph_.draw(file_name + '-graph.png')
# print(starts)

# with open('chr5', 'r') as fa:
#     reads = [read.strip() for read in fa]
# graph, starts = ov.overlap_graph(reads, 49)
#
# chr = ov.assemble_circular_chr(graph)
# print(len(chr))
# with open('chr5.ass', 'w') as fa:
#      fa.write(chr)
#
# with open('chr1', 'r') as fa:
#     reads = [read.strip() for read in fa]
# graph, starts = ov.overlap_graph(reads, 49)
# chr = ov.assemble_circular_chr(graph)
# with open('chr1.ass', 'w') as fa:
#      fa.write(chr)

# for i in range(6):
#     with open('assembled/chr{}.ass'.format(i),'r') as ass, open('assembled/chr{}.fa'.format(i), 'w') as fa:
#         chr = ass.readline()
#         fa.write('>chr {} length {}\n'.format(i, len(chr)))
#         for j in range(math.ceil(len(chr) / 80)):  # Interesting int(21 / 5) + (21 % 5 > 0)
#             fa.write(chr[80 * j: 80 * (j + 1)] + '\n')


# graph_.draw('chr3-graph_half_simplified.png')
# from graph_tool.all import *
