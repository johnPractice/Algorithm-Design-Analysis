from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.graph_length=0
    def add_edge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph.update({u:[]})
            self.graph[u].append(v)
        self.graph_length+=1
    def print_graph(self):
        print(self.graph)

    def _dfs_util(self,v,visited):
        visited.add(v)
        print(v)
        for neighbour  in   self.graph[v] :
            if neighbour not in visited:
                self._dfs_util(neighbour,visited)
                
    def dfs(self):
        visited=set()
        for v in list(self.graph):
            if v not in visited:
                self._dfs_util(v,visited)

    def bfs(self,s):
        base_root=s
        visited=[False]*(100)
        # visited=[False] * (max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            # if s not in p_s and s not in self.graph[base_root]:
            #     p_s_c+=1
            #     print('s is : {} and c is : {}'.format(s,p_s_c))
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

        



def main():
    g=Graph()
    g.add_edge(0,2)
    g.add_edge(3,1)
    g.add_edge(1,0)
    g.add_edge(1,5)
    g.add_edge(5,6)
    # g.dfs()
    g.bfs(3)
if __name__ == "__main__":
    main()