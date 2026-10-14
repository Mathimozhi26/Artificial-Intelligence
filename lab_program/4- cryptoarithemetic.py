from itertools import permutations

for S,E,N,D in permutations(range(10),4):
    if S==0: continue
    send=1000*S+100*E+10*N+D
    more=10652-send
    if 1000<=more<=9999:
        M,O,R,E=map(int,str(more))
        if len({S,E,N,D,M,O,R})==7 and M!=0:
            money=10000*M+1000*O+100*N+10*E+2
            if send+more==money:
                print(send,"+",more,"=",money)
