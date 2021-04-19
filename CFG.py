import Rule

class CFG:
    V=set()
    alphabet=set()
    R=set()
    S=''
    def __init__(self,v,alpha,r,s):
        self.V=v.copy()
        self.alphabet=alpha.copy()
        self.R=r.copy()
        self.S=s
    def accept(self,w):
        n=len(w)
        w=' '+w
        table=[[set()for i in range(n+1)]for j in range(n+1)]
        
        #fill line 1
        for i in range(1,n+1):
            for x in self.R:
                if x.endwith(w[i]):
                    table[1][i].add(x.head)
        
        for i in range(2,n+1):
            for j in range(1,n-i+2):
                l0=lambda I,J:(J,I+J-1)
                i0,j0=l0(i,j)
                for x in self.R:
                    lst=x.dRules()
                    b=False
                    for t in lst:
                        #t is rule_body
                        
                        for k in range(i0,j0):
                           l=lambda i,j:(j-i+1,i)
                           i1,j1=l(i0,k)
                           i2,j2=l(k+1,j0)
                           if t[0] in table[i1][j1] and t[1] in table[i2][j2]:
                               b=True
                               break
                    if b==True:
                        table[i][j].add(x.head)
        print(table)

        if self.S in table[n][1]:
            return True
        else:
            return False


        print(table)
    def __repr__(self):
        str=''
        for x in self.R:
            str+=x
        return str
    


