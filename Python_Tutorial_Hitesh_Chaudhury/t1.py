# # problem 1
# # str1 = input("Enter a word : ")
# # str2 = input("Enter another word : ")
# # print("Display Pattern")
# # len1 = len(str1)
# # len2 = len(str2)
# #
# # if len1 > len2:
# #     for i in range(0, len2):
# #         print(f"Index {i}: " + str1[i] + str1[i] + " - " + str2[i] + str2[i])
# #
# #     for i in range(len2, len1):
# #         print(f"Index {i}: " + str1[i] + str1[i] + " - " + "?" + "?")
# # else:
# #     for i in range(0, len1):
# #         print(f"Index {i}: " + str1[i] + str1[i] + " - " + str2[i] + str2[i])
# #
# #     for i in range(len1, len2):
# #         print(f"Index {i}: " + "?" + "?" + " - " + str2[i] + str2[i])
#
# # problem 2
# # start = int(input("Enter start integer: "))
# # end = int(input("Enter end integer: "))
# # c1 = input("Enter a letter: ")
# # c2 = input("Enter another letter: ")
# # print("Here is the output pattern:")
# #
# # dif = end - start
# # dimension = 2 * dif + 2
# # dimension += 1  # to iterate from 1 to dimension
# #
# # for i in range(1, dimension):
# #     num = start
# #     for j in range(1, i + 2):
# #         if i % 2 == 0:
# #             print(c2, end=' ')
# #             break
# #         elif i % 2 == 1 and j % 2 == 0:
# #             print(c1, end=' ')
# #         else:
# #             print(num, end=' ')
# #             num += 1
# #     print()
#
# # # problem 3
# # num = int(input("Enter an integer: "))
# # i = 1
# # while num >= 10:
# #     if num % 2 == 0:
# #         print(f"Step {i}: {num} even, divided by 2 -> {num}/{2} = {num//2}")
# #         num = num // 2
# #         i += 1
# #     elif num % 2 == 1:
# #         print(f"Step {i}: {num} odd, minus 5 -> {num}-{5} = {num-5}")
# #         num = num - 5
# #         i += 1
# # print(f"Step {i}: {num} is less then 10 -> stop now")
#
# # BFS
# # Python3 Program to print BFS traversal
# # from a given source vertex. BFS(int s)
# # traverses vertices reachable from s.
#
# class Graph:
#     def __init__(self, num_nodes, edges):
#         self.num_nodes = num_nodes
#         self.data = [[] for _ in range(num_nodes)]
#         for a, b in edges:
#             self.data[a].append(b)
#             self.data[b].append(a)
#
#     # def __repr__(self):
#     #     return "\n".join(["{}: {}".format(node, neigbours) for node, neigbours in
#     #                       enumerate(self.data)])  # it gives value and indices of the list
#     #
#     # def __str__(self):
#     #     return self.__repr__()
#
#     def add_edge(self, start, end):
#         if start < 0 or start >= self.num_nodes or end < 0 or end >= self.num_nodes:
#             print("Value error")
#         else:
#             self.data[start].append(end)
#             self.data[end].append(start)
#
#     def bfs(self, root):
#         queue = []
#         visited = [False] * len(self.data)
#
#         visited[root] = True
#         queue.append(root)
#         idx = 0
#
#         while idx < len(queue):
#             current = queue[idx]
#             idx += 1
#
#             for node in self.data[current]:
#                 if not visited[node]:
#                     visited[node] = True
#                     queue.append(node)
#
#         return queue
#
#     def dfs_recursive(self, root, visited=None):
#
#         if visited is None:
#             visited = set()
#
#         visited.add(root)
#         result = [root]
#
#         for neighbour in self.data[root]:
#             if neighbour not in visited:
#                 result += self.dfs_recursive(neighbour, visited)
#
#         return result
#
#
# if __name__ == '__main__':
#     num_nodes = 5
#     edges = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 3), (1, 4), (3, 4)]
#     graph1 = Graph(num_nodes, edges)
#     # print(graph1.bfs(3))
#     print(graph1.dfs_recursive(0))

# res = []
# n = 4
# board = [['.'] * n for i in range(n)]
# copy = [".".join(row) for row in board]
# res.append(copy)
# for i in range(len(res)):
#     for j in range(len(res[i])):
#         print(res[i][j],end='')
#         print()

from queue import Queue


def GreedyBFS(romaniaMap, StartingNode, DestinationNode):
    visited = {}    # for keeping track of the visited nodes,
    distance = {}   # keeping track of the level from root node
    parent = {}     # keeping track of the parents of a node

    BFS_result = []     # result of level order traversal
    queue = Queue()     # to maintain level order traversal

    for city in romaniaMap.keys():
        visited[city] = False   # initially making every city unvisited
        distance[city] = -1     # initially making every city level = -1
        parent[city] = None     # initially making every city with no parent

    StartingCity = StartingNode
    visited[StartingCity] = True    # Marked the starting city visited
    distance[StartingCity] = 0      # root node level = 0
    queue.put(StartingCity)         # start of bfs queue

    while not queue.empty():
        CurrentCity = queue.get()     # taking out the first item of the queue
        BFS_result.append(CurrentCity)

        for Neighbour in romaniaMap[CurrentCity]:     # visiting adjacent nodes of CurrentCity
            if not visited[Neighbour]:
                visited[Neighbour] = True
                parent[Neighbour] = CurrentCity
                distance[Neighbour] = distance[CurrentCity] + 1
                queue.put(Neighbour)

    g = DestinationNode
    finalResult = []
    while g is not None:    # g will be None for the starting city
        finalResult.append(g)   # going backwards
        g = parent[g]

    finalResult.reverse()
    print(finalResult)


if __name__ == '__main__':
    romaniaMap = {
        'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
        'Zerind': ['Arad', 'Oradea'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
        'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Iasi', 'Urziceni'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']
    }
    StartNode = 'Arad'
    DestinationNode = 'Bucharest'
    GreedyBFS(romaniaMap, StartNode, DestinationNode)
