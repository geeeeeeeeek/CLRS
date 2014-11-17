__author__ = 'Tong'
import random


class Individual():
    chromosome = ""
    fitness = 0
    p_fitness = 0

    def __init__(self, s_chromosome):
        segment = ""
        for index in range(s_chromosome):
            segment += random.randint(0, 1).__str__()
        self.chromosome = segment

    def __str__(self):
        return "chromosome[" + self.chromosome + "], fitness = " + self.fitness.__str__() \
               + ", probability of fitness = " + self.p_fitness.__str__()


def eval_fitness(chromosome, capacity, items):
    value = 0
    weight = 0
    for index in range(len(chromosome)):
        if chromosome[index] == "1":
            value += items[index][1]
            weight += items[index][0]
            if weight > capacity:
                return 0
    return value


def ga(capacity, items):
    # Parameters of the revolution.
    # Probability of crossing, Probability of mutation, Size of chromosome, Size of population, Generations.
    p_cross = 0.5
    p_mutate = 0.005
    s_chromosome = 50
    s_population = 50
    generations = 50000

    # Initialize the population.
    population = []
    for index in range(s_population):
        individual = Individual(s_chromosome)
        population.append(individual)

    depth = 0
    while depth < generations:
        sum_fitness = 0
        # Evaluate the fitness of each individual.
        for index in range(s_population):
            individual.fitness = eval_fitness(individual.chromosome, capacity, items)
            sum_fitness += individual.fitness
        # Selection
        temp = []
        for index in range(s_population):
            # Evaluate each probability of fitness.
            individual = population[index]
            individual.p_fitness = individual.fitness / sum_fitness
            times = int(individual.p_fitness * len(population))
            for it in range(times):
                temp.append(individual)
        population = temp
        # If the cast above causes individual decreases, create new ones.
        while len(population) < s_population:
                population.append(population[random.randint(0, len(population) - 1)])
        # Crossing
        for index in range(int(s_population / 2)):
            if index * 2 + 1 >= s_population:
                return
            chromosome1 = population[index * 2].chromosome
            chromosome2 = population[index * 2 + 1].chromosome
            for ptr in range(s_chromosome):
                indicator = random.random()
                if indicator <= p_cross:
                    chromo_temp = chromosome1
                    chromosome1 = chromosome1[:ptr] + chromosome2[ptr:]
                    chromosome2 = chromosome2[:ptr] + chromo_temp[ptr:]
        # Mutation
        for index in range(s_population):
            indicator = random.random()
            if indicator <= p_mutate:
                population[index] = Individual(s_chromosome)
        # Output
        optimal = population[0]
        for index in range(s_population):
            if population[index].fitness > optimal.fitness:
                optimal = population[index]
        print("Generation " + depth.__str__() + ", optimal individual is " + optimal.__str__())
        depth += 1
    print("Revolution ended!")
    return 0


# ##################################################### #
# #                      Test sets                    # #
# ##################################################### #
def test():
    capacity = 1000
    items = []
    for index in range(50):
        item_weight = random.randint(0, 30)
        item_value = random.randint(0, 5)
        items.append([item_weight, item_value])
    ga(capacity, items)


test()