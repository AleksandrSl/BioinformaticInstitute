import random
from collections import defaultdict
from copy import deepcopy


def gen_kmer_from_read(read, k):
    return [read[i:i+k] for i in range(len(read) - k + 1)]


def gen_kmers_from_reads(reads, k):
    kmers = []
    for read in reads:
        kmers.extend(gen_kmer_from_read(read, k))
    return kmers


def de_bruijn_ize(reads):
    graph = defaultdict({'in':[], 'out':[]})
    for read in reads:
        suf = read[1:]
        pref = read[:-1]
        graph[pref]['out'].append(suf)
        graph[suf]['in'].append(pref)
    return graph


def de_bruijn_ize_2(reads, k):
    graph = defaultdict(dict)
    for read in reads:
        for kmer in (read[i:i + k] for i in range(len(read) - k + 1)):
            suf = kmer[1:]
            pref = kmer[:-1]
            if suf not in graph:
                graph[suf] = {'in': set(), 'out': set()} # Заменил на set чтобы не было повторов
            if pref not in graph:
                graph[pref] = {'in': set(), 'out': set()}
            graph[pref]['out'].add(suf)
            graph[suf]['in'].add(pref)
    return graph


def de_bruijn_ize_3(reads, k):
    graph = {}
    for read in reads:
        for kmer1, kmer2 in ((read[i:i + k], read[i + 1: i + k + 1]) for i in range(len(read) - k)):
            if kmer1 not in graph:
                graph[kmer1] = {'in': defaultdict(int) , 'out': defaultdict(int)} # Заменил на set чтобы не было повторов
            if kmer2 not in graph:
                graph[kmer2] = {'in': defaultdict(int), 'out': defaultdict(int)}
            graph[kmer1]['out'][kmer2] += 1
            graph[kmer2]['in'][kmer1] += 1
    return graph

def eulerian_cycle(graph):
    eul_cycle = []
    node = random.choice(list(graph.keys()))
    eul_cycle.append(node)
    insert_point = len(eul_cycle)
    while graph != {}:
        while node in graph:
            next_node = graph[node]["out"].pop()
            if not graph[node]["out"]:          # if graph[node]["out"] == 0
                graph.pop(node)
            node = next_node
            eul_cycle.insert(insert_point, node)
            insert_point += 1
        for i in range(len(eul_cycle)):
            if eul_cycle[i] in graph:
                node = eul_cycle[i]
                insert_point = i + 1
                break
    return eul_cycle


def eulerian_path(graph):
    eul_cycle = []
    not_visited = deepcopy(graph)
    print(graph)

    next_node = None
    for item in graph.items():
        if not item[1]["out"]:
            break_point = item[0]
            not_visited.pop(item[0])
    #print(break_point)
    print(not_visited)
    node = random.choice(list(not_visited.keys()))
    eul_cycle.append(node)
    insert_point = len(eul_cycle)
    while not_visited != {}:
        if node == next_node:
            node = random.choice(list(not_visited.keys()))
            insert_point = len(eul_cycle)
        while node in not_visited:
            next_node = not_visited[node]["out"].pop()
            if not not_visited[node]["out"]:  # if graph[node]["out"] == 0
                not_visited.pop(node)
            node = next_node
            eul_cycle.insert(insert_point, node)
            insert_point += 1
        for i in range(len(eul_cycle)):
            if eul_cycle[i] in not_visited:
                node = eul_cycle[i]
                insert_point = i + 1
                break
        print(eul_cycle)
    break_point = eul_cycle.index(break_point) + 1
    return eul_cycle[break_point:] + eul_cycle[:break_point ]


def eulerian_path2(graph):
    eul_walk = []
    stack = []
    not_visited = deepcopy(graph)
    node = None
    start_node = None
    for key, val in graph.items():
        #print(sum(item[1]["out"].values()) - sum(item[1]["in"].values()))
        if (sum(val["out"].values()) - sum(val["in"].values())) == 1:
            node = key
            #print('not random node', node)
    if node is None:
        node = next(iter(not_visited))
        #print('random node', node)
    stack.append(node)

    while sum(not_visited[node]["out"].values()) != 0 or (len(stack) != 0):
        if not not_visited[node]["out"]:
            eul_walk.append(node)
            node = stack.pop()
        else:
            stack.append(node)
            for new_node in not_visited[node]["out"]:
                not_visited[node]["out"][new_node] -= 1
                node = new_node
                break
    eul_walk.reverse()

    return eul_walk


def reconstr_from_reads(reads):
    if type(reads) == str:
        reads = reads.splitlines()
    graph = de_bruijn_ize(reads)
    eulerian_path = eulerian_path2(graph)
    reconstr = ""
    for kmer in eulerian_path:
        reconstr += kmer[0]
    reconstr += eulerian_path[-1][1:]
    return reconstr


def reconstr_from_reads_2(reads, k):
    if type(reads) == str:
        reads = reads.splitlines()
    graph = de_bruijn_ize_3(reads, k)
    eulerian_path = eulerian_path2(graph)
    reconstr = ""
    for kmer in eulerian_path:
        reconstr += kmer[0]
    reconstr += eulerian_path[-1][1:]
    return reconstr


def hammingDist(seq1, seq2):
    assert len(seq1) == len(seq2)
    hamDist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamDist += 1
    return hamDist


def max_non_branching_paths(graph):
    paths = []
    nodes_in_cycles = set()
    print(graph)
    cycles = []
    for node in graph:
        if (len(graph[node]["in"]) != 1) or (len(graph[node]["out"]) != 1):
            #print(node)
            if graph[node]["out"]:
                #print("!",node)
                for out in graph[node]["out"]:
                    non_branch_path = [node]
                    next_n = out
                    while (len(graph[next_n]["in"]) == 1) and (len(graph[next_n]["out"]) == 1):
                        non_branch_path.append(next_n)
                        next_n = graph[next_n]["out"][0]
                    non_branch_path.append(next_n)
                    paths.append(non_branch_path)
        elif (len(graph[node]["in"]) == 1) and (len(graph[node]["out"]) == 1):
            if node not in nodes_in_cycles:
                start_n = node
                is_cycle = True
                out = graph[start_n]["out"][0]
                non_branch_path = [node]
                while out != start_n:
                    if (len(graph[out]["in"]) == 1) and (len(graph[out]["out"]) == 1):
                        non_branch_path.append(out)
                        out = graph[out]["out"][0]
                    else:
                        is_cycle = False
                        break
                if is_cycle:
                    non_branch_path.append(out)
                    m = str(min(list(map(int,non_branch_path))))
                    #print(non_branch_path)
                    #print(m)
                    m_i = non_branch_path.index(m)
                    if m_i != 0:
                        non_branch_path = non_branch_path[m_i:] + non_branch_path[1:m_i] + [m]
                    cycles.append(non_branch_path)
                    #print("!",non_branch_path)

                    nodes_in_cycles.update(non_branch_path)
    paths.extend(cycles)
    return paths


def gen_contigs(reads):
    short_reads = []
    #for read in reads:
    #    short_reads.extend(l2.composition(read, max(2,len(read)//2)))
    #print(short_reads)
    graph = de_bruijn_ize(reads)
    paths = max_non_branching_paths(graph)
    for path in paths:
        reconstr = ""
        for kmer in path:
            reconstr += kmer[0]
        reconstr += path[-1][1:]
        print(reconstr)

