import numpy as np
import queue


def adj_list(n, edge_list):
    adjlist = [[] for i in np.arange(n)]
    for edge in edge_list:
        adjlist[edge[0]].append(edge[1])
        adjlist[edge[1]].append(edge[0])
    return adjlist


def return_path(adjlist, s, t, search):
    visited = [False] * len(adjlist)
    prev = [-1] * len(adjlist)
    prev[s] = s
    search(adjlist, s, visited, prev)
    if not visited[t]:
        return []
    path = []
    curr = t
    while curr != s:
        path.append(curr)
        curr = prev[curr]
    path.append(curr)
    return path.reverse()


def dfs(adjlist, curr, visited, prev):
    visited[curr] = True
    for edge in adjlist[curr]:
        if not visited[edge]:
            prev[edge] = curr
            dfs(adjlist, edge, visited, prev)


def bfs(adjlist, start, visited, prev):
    que = queue.Queue()
    que.put([start, start])
    while not que.empty():
        [prev_node, curr] = que.get()
        if not visited[curr]:
            visited[curr] = True
            prev[curr] = prev_node
            for edge in adjlist[curr]:
                que.put([curr, edge])
