class Rule:
    head=' '
    body=[]
    def __init__(self,line):
        #delete extra space
        
        
        new_line=''
        for i in range(len(line)):
            if line[i]!=' ':
                new_line+=line[i]

        #secend part
        self.head=new_line[0]
        temp=new_line[3:]
        self.body=temp.split('|')
       
    def __repr__(self):
        str=self.head+'->'
        for x in self.body:
            str+=x+'|'
        return str
    def endwith(self,char):
        b=False
        for x in self.body:
            if x==char:
                b=True
                break
        return b

    def copy(self):
        res=Rule('s->')
        res.body=self.body.copy()
        res.head=self.head
        return res
    def dRules(self):
        d_body=[]
        for x in self.body:
            if len(x)!=1:
                d_body.append(x)
        return d_body

