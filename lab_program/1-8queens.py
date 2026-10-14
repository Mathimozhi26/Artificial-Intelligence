from collections import deque
s=(1,2,3,4,0,5,6,7,8); g=(1,2,3,4,5,6,7,8,0)
q=deque([s]); seen={s}
while q:
 x=q.popleft()
 if x==g: print("Solved:",x); break
 i=x.index(0)
 for j in range(9):
  if abs(i-j) in (1,3):
   y=list(x); y[i],y[j]=y[j],y[i]; y=tuple(y)
   if y not in seen: seen.add(y); q.append(y)
