from collections import deque
q=deque([((3,3,1),[])])
while q:
 (m,c,b),p=q.popleft()
 if (m,c,b)==(0,0,0): print(p+[(m,c,b)]); break
 for a,z in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
  x,y=m+(-1 if b else 1)*a,c+(-1 if b else 1)*z
  if 0<=x<=3 and 0<=y<=3 and (x==0 or x>=y) and (3-x==0 or 3-x>=3-y):
   q.append(((x,y,1-b),p+[(m,c,b)]))
