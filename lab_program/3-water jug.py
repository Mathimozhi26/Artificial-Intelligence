from collections import deque
q=deque([((0,0),[])])
while q:
 (a,b),p=q.popleft()
 if a==2: print(p+[(a,b)]); break
 for x in [(5,b),(a,3),(0,b),(a,0),(min(5,a+b),max(0,a+b-5))]:
  if x not in [z[0] for z in q]: q.append((x,p+[(a,b)]))
