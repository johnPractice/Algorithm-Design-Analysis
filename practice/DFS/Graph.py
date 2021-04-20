from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.graph_vertex=defaultdict(list)
        self.graph_level=defaultdict()
    def add_edge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph.update({u:[]})
            self.graph[u].append(v)
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
        visited=[False] * (max(self.graph)+1)
        l=0
        queue=[]
        root_begin=s
        self.graph_vertex[root_begin]=[]
        queue.append(s)
        self.graph_level[s]={l:[s]}
        while queue:
            s=queue.pop(0)
            # print(s)
            self.graph_vertex[root_begin].append(s)
            # print (s, end = " ")
            # for i in range(len(self.graph[s])):
            #     l+=1
            #     if visited[i]==False:
            #         queue.append(self.graph[s][i])
            #         if l in  self.graph_level[s]:
            #            self.graph_level[s][l].append(self.graph[s][i])
            #         else:
            #             self.graph_level[s].update({l:[]})
            #             self.graph_level[s][l].append(self.graph[s][i])
            #         visited[i]=True        
            for i in (self.graph[s]):
                # print(i)
                if visited[l]==False:
                    queue.append(i)
                    visited[l]=True
                l+=1
        return self.graph_vertex[root_begin]
        
    def print_path(self,s,v):
        self.bfs(s)
        # print(self.graph_vertex)
        if v==s:
            print(v)
        elif v  in self.graph_vertex[s]:
            i=self.graph_vertex[s].index(v)
            return(self.graph_vertex[s][:i+1])
            
        else:
            print('no path')


def main():
    g=Graph()
    g.add_edge(0,10)
    g.add_edge(0,12)
    g.add_edge(1,31)
    g.add_edge(3,1)
    # g.add_edge(10,11)
    # g.add_edge(10,12)
    # g.dfs()
    print(g.bfs(0))
    # g.print_path(10,11)
if __name__ == "__main__":
    main()