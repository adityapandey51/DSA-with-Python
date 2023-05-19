import numpy as np
def floyd(graph,numberOfNodes):
    for k in range(numberOfNodes):
        for i in range(numberOfNodes):
            for j in range(numberOfNodes):
                #comparing the direct distance  with distance through the intermediary point
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    return graph
g=[[0, 2,np.Inf, 6, np.Inf],
               [2, 0, 3, 8, 5],
               [np.Inf, 3, 0, np.Inf, 7],
               [6, 8, np.Inf, 0, 9],
               [np.Inf, 5, 7, 9, 0]]
print(floyd(g,5))


 