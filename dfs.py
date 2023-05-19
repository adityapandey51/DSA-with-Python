adjancy_list={
  0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}

def dfs(node,adjancy_list):
    visited_dic={}
    visited=[]
    stack=[]
    nodes=list(adjancy_list)
    for i in nodes:
        visited_dic[i]=False
    stack.insert(0,node)
    visited_dic[node]=True
    while len(stack)!=0:
        s=stack.pop(0)
        visited.append(s)
        for i in adjancy_list[s]:
            if visited_dic[i]==False:
                stack.insert(0,i)
                visited_dic[i]=True
    return visited
print(dfs(0,adjancy_list))
