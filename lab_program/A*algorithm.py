import heapq
g={'A':[('B',1),('C',3)],'B':[('D',2)],'C':[('D',1)],'D':[]}
h={'A':3,'B':2,'C':1,'D':0}
q=[(3,0,'A')]
while q:
 f,c,n=heapq.heappop(q)
 if n=='D':
  print("Cost:",c); break
 for x,w in g[n]:
  heapq.heappush(q,(c+w+h[x],c+w,x))
