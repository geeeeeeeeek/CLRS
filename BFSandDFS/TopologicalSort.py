__author__ = 'Tong'

''''Write code for the topological sort of a directed acyclic graph (recursive version) and use the
    data shown in Figure 1 to test your implementation. '''


class Vertex:
    data = ""
    stack_in = 0
    stack_out = 0
    prev = None
    next = []

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "[" + self.data + "] : " + "in = " \
               + self.stack_in.__str__() + ", out = " + self.stack_out.__str__()


class Graph:
    in_vertices = []

    def __init__(self, in_vertices):
        self.in_vertices = in_vertices


def dfs(vertex):
    global degree, stack, graph
    stack.append(vertex)
    vertex.stack_in = degree
    degree += 1
    if vertex.next:
        for each in vertex.next:
            if not each.stack_in:
                dfs(each)
    while stack:
        vertex = stack.pop()
        if vertex.next and not vertex.next[-1].stack_out:
            stack.append(vertex)
            return
        vertex.stack_out = degree
        degree += 1
        bin.append(vertex)

# TEST
thesis = Vertex("Thesis")
internship = Vertex("Internship", [thesis])
ac = Vertex("ALL COURSES", [internship, thesis])
wa = Vertex("Web Application")
pm = Vertex("Project Management")
ins = Vertex("Intelligent Systems")
se = Vertex("Software Engineering", [pm, ins])
oop = Vertex("Object Oriented Programming", [wa, se])
db = Vertex("Database", [wa, se])
ds = Vertex("Data Structure and Algorithm", [ins, se])
joc = Vertex("Java or C++", [wa, oop, ds])
cn = Vertex("Computer Network", [se])
ca = Vertex("Computer Architecture")
cs = Vertex("Computer Systems", [se, cn, ca])
ps = Vertex("Probability and Statistics", [ins, ds])
calculus = Vertex("Calculus", [ps, ca])
dm = Vertex("Discrete Mathematics", [ins])

stack = []
bin = []
degree = 1
graph = Graph([ac, joc, db, cs, dm, calculus])

for v in graph.in_vertices:
    dfs(v)
bin.sort(key=lambda x: x.stack_out, reverse=True)
file_handler = open('output/result1.txt', 'w', -1, "utf-8")
output = ""
for b in bin:
    output += b.__str__() + "\n"
file_handler.write(output)
file_handler.close()
