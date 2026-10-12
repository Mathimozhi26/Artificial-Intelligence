g={'A':['B','C'],'B':['A','C'],'C':['A','B']}
colors=['Red','Green','Blue']
r={}
for a in g:
 for c in colors:
  if all(r.get(n)!=c for n in g[a]):
   r[a]=c; break
print(r)
