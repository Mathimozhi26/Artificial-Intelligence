def minimax(t,m):
 if isinstance(t,int): return t
 v=[minimax(x,not m) for x in t]
 return max(v) if m else min(v)
print(minimax([[3,5],[2,9]],True))
