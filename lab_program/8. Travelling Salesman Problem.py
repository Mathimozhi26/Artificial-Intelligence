from itertools import permutations
c=[[0,10,15],[10,0,20],[15,20,0]]
p=min((sum(c[r[i]][r[i+1]] for i in range(3)),r)
 for r in [(0,)+x+(0,) for x in permutations([1,2])])
print("Cost:",p[0],"Route:",p[1])
