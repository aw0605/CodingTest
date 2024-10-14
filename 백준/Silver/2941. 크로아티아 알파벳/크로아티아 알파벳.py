s = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in croatia :
    s = s.replace(a, '*')

print(len(s))