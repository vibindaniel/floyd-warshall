import json
from random import randint


class Program():
    a = []
    b = []
    k = 0
    N = 0
    d = ''
    next = []
    link_cost = []

    def __init__(self, data):
        self.k = data["k"]
        self.N = data["N"]
        self.d = str(data["d"]) * 2

        # initializing arrays a, b and next
        for i in range(0, self.N):
            self.a.append([])
            self.b.append([])
            self.next.append([])
            self.link_cost.append([])
            for j in range(0, self.N):
                self.a[i].append(0)
                self.b[i].append(0)
                self.next[i].append(0)
                self.link_cost[i].append(0)

    def initialize_parameters(self):
        # assigning 1 to a[i][j]
        # where j = k random values of indices and
        # j is not i
        for i in range(0, self.N):
            for k in range(0, self.k):
                j = randint(0, self.N - 1)
                while j is i and self.a[i][j] is 1:
                    j = randint(0, self.N - 1)
                self.a[i][j] = 1

        # assigning b[i][j] = |d[j] - d[i]|
        # and a[i][j] = 100 where i is not j
        for i in range(0, self.N):
            for j in range(0, self.N):
                self.b[i][j] = abs(int(self.d[j]) - int(self.d[i]))
                self.next[i][j] = j
                if self.a[i][j] is not 1:
                    self.a[i][j] = 100

    def start_algorithm(self):
        a = self.a
        b = self.b
        N = self.N
        next = self.next

        # http://masc.cs.gmu.edu/wiki/FloydWarshall
        # https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
        for k in range(0, N):
            for i in range(0, N):
                for j in range(0, N):
                    if (a[i][j] > a[i][k] + a[k][j]):
                        a[i][j] = a[i][k] + a[k][j]
                        next[i][j] = next[i][k]
        self.get_link_cost()
        self.get_opt_cost()

    def get_link_cost(self):
        for i in range(0, self.N):
            for j in range(0, self.N):
                if i is not j and self.next[i][j] is not 0:
                    p = i
                    n = self.next[i][j]
                    sum = 0
                    while n is not j:
                        sum += self.a[p][n]
                        p = n
                        n = self.next[n][j]
                    sum += self.a[p][n]
                    self.link_cost[i][j] = sum * self.b[i][j]

    def get_opt_cost(self):
        opt_cost = 0
        for i in range(0, self.N):
            opt_cost += sum(self.link_cost[i])
        print(opt_cost)


if __name__ == '__main__':
    with open('config.json') as data:
        p = Program(json.load(data))
        p.initialize_parameters()
        p.start_algorithm()
