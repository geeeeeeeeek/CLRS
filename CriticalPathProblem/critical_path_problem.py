__author__ = 'Tong'
# A critical path #
# is a longest path through the dag, corresponding to the longest time to perform an ordered sequence of jobs.
# (The TA thought) It would be more natural for vertices to represent jobs and edges to represent
# sequencing constraints; that is, edge (u, v) would indicate that job u must be performed before job v.
# Weights would then be assigned to vertices, not edges.
#
# Here I give an algorithm that can finds a longest path in a directed acyclic graph with weighted vertices
# in linear time. The algorithm referenced to 'Shortest Path Faster Algorithm' published in 1994 by Fanding Duan.


class MyAlgorithm:
    @staticmethod
    def get_critical_path(graph):
        v = {}
        for each in graph.get('v'):
            v[each] = Vertex(each, float('-inf'))
        s = Vertex(graph.get('v')[0])
        v[s.u] = s
        for each in graph.get('e'):
            v.get(each[0]).v.append(each[1])

        q = {s.u: v.get(s.u)}
        while q:
            u = q.popitem()[1]
            for e in u.v:
                if u.d + e > v.get(e).d:
                    v.get(e).prev = u.u
                    v.get(e).d = u.d + e
                    if q.get(e) is None:
                        q[e] = v.get(e)

        last = s
        for each in v.values():
            if each.d > last.d:
                last = each
        trace = [last.u]
        while last != s:
            last = v.get(last.prev)
            trace.append(last.u)

        return trace[::-1]


class Vertex:
    def __init__(self, u, d=0.0):
        self.u = u
        self.d = d
        self.v = []
        self.prev = 0