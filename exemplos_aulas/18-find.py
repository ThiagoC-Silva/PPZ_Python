#FIND AND REPLACE
s = 'Um tigre, dois tigres, três tigres'

print(s.find('tigre'))
print(s.find('tigre', 16))

print(s.replace('tigre','gato'))

s = s.replace('tigre', 'cachorro')
print(s)