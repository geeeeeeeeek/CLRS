__author__ = 'Tong'

'''(Farmer,Wolf,Goat,Cabbage)'''
'''A farmer with its wolf, goat, and cabbage come to the edge of a river they wish to
    cross. There is a boat at the river’s edge, but, of course, only the farmer can row. the
    boat also can carry only two things (including the rower) at a time. If the wolf is ever
    left alone with the goat, the wolf will eat the goat; similarly, if the goat is left alone
    with the cabbage, the goat will eat the cabbage. Devise a sequence of crossings of the
    river so that all four characters arrive safely on the other side of the river. '''
WEST = False
EAST = True


class State:
    past_states = []

    def add_(self, state):
        self.past_states.append(state)

    def del_(self, state):
        self.past_states.remove(state)

    @staticmethod
    def is_safe(state):
        farmer, wolf, goat, cabbage = state
        return not (farmer ^ goat) or wolf ^ goat and goat ^ cabbage

    def is_valid(self, state):
        return state not in self.past_states

    def next(self, state):
        farmer, wolf, goat, cabbage = state
        next_farmer = (not farmer, wolf, goat, cabbage)
        next_wolf = (not farmer, not wolf, goat, cabbage)
        next_goat = (not farmer, wolf, not goat, cabbage)
        next_cabbage = (not farmer, wolf, goat, not cabbage)
        results = []

        if self.is_safe(next_farmer) and self.is_valid(next_farmer):
            results.append(next_farmer)
        if self.is_safe(next_wolf) and self.is_valid(next_wolf) and farmer == wolf:
            results.append(next_wolf)
        if self.is_safe(next_goat) and self.is_valid(next_goat) and farmer == goat:
            results.append(next_goat)
        if self.is_safe(next_cabbage) and self.is_valid(next_cabbage) and farmer == cabbage:
            results.append(next_cabbage)
        return results


stack = []
state = State()
init_state = (WEST, WEST, WEST, WEST)


def dfs(s):
    state.add_(s)
    stack.append(s)
    n = state.next(s)
    if n:
        for each in n:
            dfs(each)
    if s == (EAST, EAST, EAST, EAST):
        file_handler = open('output/result2.txt', 'w', -1, "utf-8")
        output = "False for in the WEST side, True for in the EAST side.\n"
        for e in stack:
            farmer, wolf, goat, cabbage = e
            output += "[Farmer:" + farmer.__str__() + "] [Wolf:" + wolf.__str__() \
                      + "] [Goat:" + goat.__str__() + "] [Cabbage:" + cabbage.__str__() + "]\n"
        file_handler.write(output)
        file_handler.close()
        exit(0)
    while stack:
        m = stack.pop()
        if state.next(m) and state.is_valid(m[-1]):
            stack.append(m)
            return
        state.del_(m)


dfs(init_state)
