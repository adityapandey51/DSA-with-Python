adjancy_list={
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}

def bfs(node,adjancy_list):
    nodes=list(adjancy_list)
    visited_dic={}
    queue=[]
    visited=[]
    for i in nodes:
        visited_dic[i]=False
    s=node
    queue.append(s)
    visited_dic[s]=True
    while len(queue) !=0:
        s=queue.pop(0)
        visited.append(s)
        for i in adjancy_list[s]:
            if visited_dic[i]==False:
                queue.append(i)
                visited_dic[i]=True
    return visited

print(bfs(0,adjancy_list))







    