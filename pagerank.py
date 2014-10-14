__author__ = 'igor'
import collections
import fractions

#presets:

#q1
#links = collections.OrderedDict([('a', ['b', 'c']), ('b', ['c']), ('c', ['c'])])
#z = 0.7
#C = 3
#q2
#links = collections.OrderedDict([('a', ['b', 'c']), ('b', ['c']), ('c', ['a'])])
#z = 0.85
#C = 1
#q3
links = collections.OrderedDict([('a', ['b', 'c']), ('b', ['c']), ('c', ['a'])])
z = 1
C = 3

# start:

N = len(links)
beta = fractions.Fraction(z)
alpha = 1 - beta
M = [[0 for n in range(N)] for m in range(N)]

i = -1
for k, v in links.items():
    i += 1
    for j in range(0, N):
        key = list(links.keys())[j]
        cfn = 1 if key in v else 0
        M[j][i] = (fractions.Fraction(cfn, len(v)) if len(v) > 0 else 0)

V = [fractions.Fraction(C, N) for n in range(0, N)]
result = V
for k in range(0, 4):
    tmpResult = list(result)
    for i in range(0, N):
        mult = 0
        for j in range(0, N):
            mult += M[i][j] * tmpResult[j]
        result[i] = (beta * mult + fractions.Fraction(alpha, N))

print(result)
print('sum', C*float(result[0] + result[1] + result[2]))

a = result[0]
b = result[1]
c = result[2]

#print('a+b', C*(float(result[0]) + float(result[1])))
#print('a+c', C*(float(result[0]) + float(result[2])))
#print('b+c', C*(float(result[1]) + float(result[2])))

#print('a = 0.9c + 0.05b', '->', float(a), ' = ', float(0.9 * c) + float(0.05 * b))
#print('a = c + 0.15b', '->', float(a), ' = ', float(1.0 * c) + float(0.15 * b))
#print('85b = 0.575a + 0.15c', '->', float(85 * b), ' = ', float(0.575 * a) + float(0.15 * c))
#print('0.95b = 0.475a + 0.05c', '->', float(0.95 * b), ' = ', float(0.475 * a) + float(0.05 * c))

print(float(a), float(b), float(c))





