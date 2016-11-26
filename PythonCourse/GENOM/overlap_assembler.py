from collections import defaultdict


def find_overlap(a, b, min_overlap):
    start = 0
    while True:
        start = a.find(b[:min_overlap], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1


def overlap_graph(reads, min_overlap):
    graph = defaultdict(list)
    start = set(reads)
    for read1 in reads:
        #print('1',read1)
        for read2 in reads:
            #print('2',read2)
            if read1 == read2:
                continue
            overlap = find_overlap(read1, read2, min_overlap)
            if overlap != 0:
                graph[read1].append((read2, overlap)) # Можно здесь оставлять только максимальное перекрывание, остальные нам вроде и не нужны?
                if read2 in start:
                    start.remove(read2)
    for read in graph:
        graph[read].sort(key=lambda x: x[1]) # Можно заменить на что то lambda?
    print('Graph is built')
    return graph, start.pop()


def assemble(overlap_graph, start):
    genome = []
    #g = Graph()
    next = start
    #v1 = g.add_vertex()
    genome.append(next)
    while overlap_graph:
        try:
            next, pos = overlap_graph[next].pop(-1)
        except IndexError:
            print('IndexError')
            #graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=5, output_size=(4000, 4000),
            #           output="two-nodes.svg")
            return ''.join(genome)
        genome.append(next[pos:])
        #v2 = g.add_vertex()
        if not next:
            print('Break')
            break
        #g.add_edge(v1,v2)
        #v1 = v2
    #graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=5, output_size=(4000, 4000), output="two-nodes.svg")
    return ''.join(genome)


if __name__ == '__main__':
    with open('test.dna', 'r') as f:
        reads = [line.strip() for line in f]
    l = 0
    for read in reads:
        l += len(read)
    print(l)
    genome = assemble(*overlap_graph(reads, 50))
    print(len(''.join(genome)))

