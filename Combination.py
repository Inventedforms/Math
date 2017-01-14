from functools import reduce
import operator


def main():
    print("720 == " + str(permutation(10, 3)))
    return


def combination_set(n, k):
    ##return list of k-subsets of a set of size n


def permutation_set(n, k):
    ##return list of k-lists from a list of size n
    for x in n:
        
    return

def combination(n, k):
    if n < 0 or k < 0 or k > n: return 0
    k = min(k, n - k)
    topVals = list(range(n, n-k, -1))
    for x in range(k, 0, -1):
        for y in topVals:
            if y % x == 0:
                topVals[topVals.index(y)] = y / x
                break
    print (topVals)
    return reduce(operator.mul, topVals)


def permutation(n, k):
    if n < 0 or k < 0: return 0
    return reduce(operator.mul, list(range(n, n-k, -1)))


main()