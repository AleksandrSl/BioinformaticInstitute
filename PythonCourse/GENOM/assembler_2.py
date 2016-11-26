from collections import defaultdict
class DeBruijnGraph:

    @staticmethod
    def chop(st, k):
        for i in range(len(st) - k + 1):
            yield st[i:i + k]

    class Node:
        def __init__(self, kmer):
            self.kmer = kmer

        def __hash__(self):
            return hash(self.kmer)

        def __str__(self):
            return self.kmer

        def __repr__(self):
            return self.kmer

    def __init__(self, strings, k):
        self.graph = defaultdict(list)
        self.nodes = {}
        self.k = k
        for st in strings:
            for kmer in self.chop(st, k):
                pref, suf = kmer[:-1], kmer[1:]
                nodeL, nodeR = None, None
                if pref in self.nodes:
                    nodeL = self.nodes[pref]
                else:
                    nodeL = self.nodes[pref] = self.Node(pref)
                if suf in self.nodes:
                    nodeR = self.nodes[suf]
                else:
                    nodeR = self.nodes[suf] = self.Node(suf)
                self.graph[nodeL].append(nodeR)

def eulerian_cycle(graph):
    tour = []
    src = next(iter(graph))
    def __visit(n):
        while len(graph[n]) > 0:
            dst = graph[n].pop()
            __visit(dst)
        tour.append(n.kmer)

    __visit(src)
    return tour[::-1][:-1]