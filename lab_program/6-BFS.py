g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
q=['A']
while q:
 n=q.pop(0)
 print(n,end=' ')
 q+=g[n]
