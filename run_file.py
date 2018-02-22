import json
from random import randint


class Program():
    a = []
    b = []
    k = 0
    N = 0
    d = ''
    next = []

    def __init__(self, data):
        self.k = data["k"]
        self.N = data["N"]
        self.d = str(data["d"]) * 2
        for i in range(0, self.N):
            self.a.append([])
            self.b.append([])
            self.next.append([])
            for j in range(0, self.N):
                self.a[i].append(0)
                self.b[i].append(0)
                self.next[i].append(0)

    def initialize_parameters(self):
        for i in range(0, self.N):
            for k in range(0, self.k):
                j = randint(0, self.N - 1)
                while j is i and self.a[i][j] is 1:
                    j = randint(0, self.N - 1)
                self.a[i][j] = 1
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
        self.a = a
        self.next = next


if __name__ == '__main__':
    with open('config.json') as data:
        p = Program(json.load(data))
        p.initialize_parameters()
        p.start_algorithm()
