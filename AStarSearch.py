__author__ = 'Tong'
import math

map_width = 10
map_height = 6
map_sample1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]

map_sample2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
               [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
               [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]


class Node():
    # x and y be the location of the node.
    x = y = -1
    # Let f be evaluation function, h be heuristic function, g be the cost to reach the node. And f = g + h.
    f = g = h = 0
    parent = None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_loc(self, x, y):
        self.x = x
        self.y = y

    def get_f(self):
        return self.f

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def set_g(self, g):
        self.g = g
        self.f = self.g + self.h

    def set_h(self, h):
        self.h = h
        self.f = self.g + self.h

    def set_parent(self, node):
        self.parent = node

    def get_parent(self):
        return self.parent

    @staticmethod
    def compare_to(node1, node2):
        return node1.get_x() == node2.get_x() and node1.get_y() == node2.get_y()

    def __str__(self):
        return "(" + self.x.__str__() + ", " + self.y.__str__() + "), f = " + self.f.__str__() + ", g = " + self.g.__str__() + ", h=" + self.h.__str__()


class State:
    map_sample1 = []
    map_width = 0
    map_height = 0
    start_node = Node()
    end_node = Node()

    frontier = []
    explored = []

    def __init__(self, sample, width, height, start_node, end_node):
        self.map_sample = sample
        self.map_width = width
        self.map_height = map_height
        self.start_node = start_node
        self.end_node = end_node
        self.frontier.append(start_node)

    # MERGE-SORT
    def recursive_merge_sort(self, a):
        if len(a) == 1:
            return a
        mid = int(len(a) / 2)
        left = a[:mid]
        right = a[mid:]
        return self.merge(self.recursive_merge_sort(left), self.recursive_merge_sort(right))

    def merge(self, left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0].get_f() < right[0].get_f():
                result.append(left[0])
                left.remove(left[0])
            else:
                result.append(right[0])
                right.remove(right[0])
        return result + left + right

    def sort(self):
        if not self.frontier:
            return
        return self.recursive_merge_sort(self.frontier)


class Agent:
    @staticmethod
    def update(node, parent_node, state):
        # if not state.frontier:
        # return -1
        for each_node in state.frontier:
            if Node.compare_to(each_node, node):
                if node.get_f() < each_node.get_f():
                    state.frontier.remove(each_node)
                    state.frontier.append(node)
                return 1
        if state.explored:
            for each_node in state.explored:
                if Node.compare_to(each_node, node):
                    if node.get_f() < each_node.get_f():
                        state.explored.remove(each_node)
                        state.frontier.append(node)
                    return 1
        state.frontier.append(node)
        return 1

    @staticmethod
    def turn_left(node, state):
        node_left = Node()
        node_left.parent = node
        node_left.set_loc(node.get_x(), node.get_y() - 1)
        node_left.set_g(eval_g(node, node_left))
        node_left.set_h(eval_h(node_left, state.end_node))
        if legal_step_test(node_left, state):
            return Agent.update(node_left, node, state)
        return 0

    @staticmethod
    def turn_right(node, state):
        node_right = Node()
        node_right.parent = node
        node_right.set_loc(node.get_x(), node.get_y() + 1)
        node_right.set_g(eval_g(node, node_right))
        node_right.set_h(eval_h(node_right, state.end_node))
        if legal_step_test(node_right, state):
            return Agent.update(node_right, node, state)
        return 0


    @staticmethod
    def turn_up(node, state):
        node_up = Node()
        node_up.parent = node
        node_up.set_loc(node.get_x() - 1, node.get_y())
        node_up.set_g(eval_g(node, node_up))
        node_up.set_h(eval_h(node_up, state.end_node))
        if legal_step_test(node_up, state):
            return Agent.update(node_up, node, state)
        return 0


    @staticmethod
    def turn_down(node, state):
        node_down = Node()
        node_down.parent = node
        node_down.set_loc(node.get_x() + 1, node.get_y())
        node_down.set_g(eval_g(node, node_down))
        node_down.set_h(eval_h(node_down, state.end_node))
        if legal_step_test(node_down, state):
            return Agent.update(node_down, node, state)
        return 0


    @staticmethod
    def turn_up_left(node, state):
        node_up_left = Node()
        node_up_left.parent = node
        node_up_left.set_loc(node.get_x() - 1, node.get_y() - 1)
        node_up_left.set_g(eval_g(node, node_up_left))
        node_up_left.set_h(eval_h(node_up_left, state.end_node))
        if legal_step_test(node_up_left, state):
            return Agent.update(node_up_left, node, state)
        return 0


    @staticmethod
    def turn_up_right(node, state):
        node_up_right = Node()
        node_up_right.parent = node
        node_up_right.set_loc(node.get_x() - 1, node.get_y() + 1)
        node_up_right.set_g(eval_g(node, node_up_right))
        node_up_right.set_h(eval_h(node_up_right, state.end_node))
        if legal_step_test(node_up_right, state):
            return Agent.update(node_up_right, node, state)
        return 0


    @staticmethod
    def turn_down_left(node, state):
        node_down_left = Node()
        node_down_left.parent = node
        node_down_left.set_loc(node.get_x() + 1, node.get_y() - 1)
        node_down_left.set_g(eval_g(node, node_down_left))
        node_down_left.set_h(eval_h(node_down_left, state.end_node))
        if legal_step_test(node_down_left, state):
            return Agent.update(node_down_left, node, state)
        return 0


    @staticmethod
    def turn_down_right(node, state):
        node_down_right = Node()
        node_down_right.parent = node
        node_down_right.set_loc(node.get_x() + 1, node.get_y() + 1)
        node_down_right.set_g(eval_g(node, node_down_right))
        node_down_right.set_h(eval_h(node_down_right, state.end_node))
        if legal_step_test(node_down_right, state):
            return Agent.update(node_down_right, node, state)
        return 0


def eval_g(parent_node, node):
    if node.parent:
        return parent_node.get_g() + math.sqrt(
            math.pow(node.get_x() - parent_node.get_x(), 2) + math.pow(node.get_y() - parent_node.get_y(), 2))
    else:
        return math.sqrt(
            math.pow(node.get_x() - parent_node.get_x(), 2) + math.pow(node.get_y() - parent_node.get_y(), 2))


def eval_h(node, end):
    return abs(node.get_x() - end.get_x()) + abs(node.get_y() - end.get_y())


def actions(state):
    if not state.frontier:
        return -1
    f = 0
    for each_node in state.frontier:
        if not goal_test(each_node, state):
            node = each_node
            f = 1
            break
    if f == 0:
        return 1
    state.frontier.remove(node)
    state.explored.append(node)

    Agent.turn_left(node, state)
    Agent.turn_right(node, state)
    Agent.turn_up(node, state)
    Agent.turn_down(node, state)
    Agent.turn_up_left(node, state)
    Agent.turn_up_right(node, state)
    Agent.turn_down_left(node, state)
    Agent.turn_down_right(node, state)
    state.frontier = state.sort()
    return 0


def legal_step_test(node, state):
    if node.get_x() in range(0, state.map_height) and node.get_y() in range(0, state.map_width):
        return state.map_sample[node.get_x()][node.get_y()]
    else:
        return 0


def goal_test(node, state):
    x = node.get_x()
    y = node.get_y()
    return x == state.end_node.get_x() and y == state.end_node.get_y()


def result(node):
    print(node)
    while node.parent:
        node = node.parent
        print(node)


# Test the algorithm
start_node = Node()
start_node.set_loc(3, 1)

end_node = Node()
end_node.set_loc(3, 7)

start_node.set_h(eval_h(start_node, end_node))
start_node.set_g(eval_h(start_node, start_node))
end_node.set_h(eval_h(end_node, end_node))
end_node.set_g(eval_h(start_node, end_node))

s = State(map_sample2, map_width, map_height, start_node, end_node)

flag = 0
while flag == 0:
    flag = actions(s)
if flag == -1:
    print("fail")
if flag == 1:
    result(s.frontier[0])