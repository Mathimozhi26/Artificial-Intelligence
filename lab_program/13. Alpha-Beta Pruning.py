def ab(t,a,b,m):
 if isinstance(t,int): return t
 v=float('-inf') if m else float('inf')
 for x in t:
  r=ab(x,a,b,not m)
  v=max(v,r) if m else min(v,r)
  if m: a=max(a,v)
  else: b=min(b,v)
  if a>=b: break
 return v
print(ab([[3,5],[2,9]],float('-inf'),float('inf'),True))
