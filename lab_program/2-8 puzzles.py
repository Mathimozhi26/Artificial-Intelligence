def q(a=[]):
 if len(a)==8: print(a); return
 for c in range(8):
  if all(c!=x and abs(c-x)!=len(a)-i for i,x in enumerate(a)):
   q(a+[c])
q()
