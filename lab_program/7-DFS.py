g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
def dfs(n):
 print(n,end=' ')
 for x in g[n]: dfs(x)
dfs('A')
