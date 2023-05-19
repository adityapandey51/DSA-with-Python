inf=999999
dis_matrix=[[inf, 2, inf, 6, inf],
               [2, inf, 3, 8, 5],
               [inf, 3, inf, inf, 7],
               [6, 8, inf, inf, 9],
               [inf, 5, 7, 9, inf]]#it is the distancee matrix of the graph for each and every point
NumberofNodes=5

visited_dic={}
for i in range (NumberofNodes):
    visited_dic[i]=False
numberOfEdges=0
visited_dic[0]=True
while(numberOfEdges<NumberofNodes-1):
    minimum=inf
    a=0
    b=0
    for i in range(NumberofNodes):
        if (visited_dic[i]):
            for j in range(NumberofNodes):
                if (not visited_dic[j]) and(dis_matrix[i][j]!=minimum):
                    if minimum>dis_matrix[i][j]:
                        minimum=dis_matrix[i][j]
                        a=i
                        b=j
    print(str(a)+"-"+str(b)+" ",dis_matrix[a][b])
    visited_dic[b]=True
    numberOfEdges+=1

