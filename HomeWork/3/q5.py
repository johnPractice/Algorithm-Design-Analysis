

def dfs(u, visit):
	
	global res, g

	visit[u] = True
	currComponentNode = 0

	for i in range(len(g[u])):
		v = g[u][i]
		
		if (not visit[v]):

			subtreeNodeCount = dfs(v, visit)

			if (subtreeNodeCount % 2 == 0):
				res += 1

	
			else:
				currComponentNode += subtreeNodeCount
	return (currComponentNode + 1)
def maxEdgeRemovalToMakeForestEven(N) :
	visit = [False for _ in range(N + 1)]
	dfs(0, visit)
	return res
	
def addEdge(u, v):
	global g
	g[u].append(v)
	g[v].append(u)

def input_user():
    n=int(input())
    edge=[[]*0 for i in range(n-1)]
    for i in range(n-1):
        n1=input().split(' ')
        for j in n1:
            edge[i].append(int(j)-1)
    return None if n%2 == 1 else edge
if __name__ == "__main__":
	res = 0
	edges = input_user()
	if edges is None:
    		print('-1')
	else:
		N = len(edges)

		g = [[] for _ in range(N + 1)]
		
		for i in range(N):
			addEdge(edges[i][0], edges[i][1])

		print(maxEdgeRemovalToMakeForestEven(N))

