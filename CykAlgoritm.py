import Rule as r
import CFG as c
r1=r.Rule('moein khorasani | avin')
v=set()
rules=set()
alpha=set()
s=''
line=input('Enter your Varibles:\n')
v=line.split(',')
line=input('Enter your alphebet:\n')
alpha=line.split(',')
s=input('Enter your start var:\n')
print('Enter your rules')
while True:
    line=input('')
    if line.upper()=='END':
        break
    else:
        tmpr=r.Rule(line)
        rules.add(tmpr)
c1=c.CFG(v,alpha,rules,s)
b=c1.accept('aaaaaaaaaacccccccc')

for i in range(10):
    print('\n')
if b==True:
    print('yes')
else:
    print('no')




