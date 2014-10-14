__author__ = 'igor'
from itertools import groupby
from functools import reduce

data = [15, 21, 24, 30, 49]


def divisor_map(inputs):
    map_result = []
    for i in inputs:
        divisors = []
        d = 2
        while d <= i:
            if i % d == 0:
                if not any(filter(lambda x: d % x == 0, divisors)):
                    divisors.append(d)
            d += 1 if d == 2 else 2
        map_result.append([(d, i) for d in divisors])
    return map_result


def divisor_reduce(map_result):
    pairs = sorted([pair for pairs in map_result for pair in pairs], key=lambda x: x[0])
    reduce_result = [(k, reduce(lambda x, y: type(x), list(v))) for k, v in groupby(pairs, lambda x: x[0])]
    return reduce_result

print(divisor_reduce(divisor_map(data)))





