"""
Generates all subsets from {0,1,2,3,....,n-1}
"""


def combinations(num):
    cmp = []
    result = []

    def search(n):
        if n == num:
            result.append(cmp[:])
        else:
            cmp.append(n)
            search(n+1)
            cmp.pop()
            search(n+1)
    search(0)
    return result


if __name__ == '__main__':
    for cmb in combinations(5):
        print(set(cmb))
    print(len(combinations(5)))