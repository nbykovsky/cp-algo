"""
generates all permutations of {0,1,2,3,...,n-1}
"""


def permutations(num):
    prm = []
    chosen = [False] * num
    result = []

    def search():
        if len(prm) == num:
            result.append(prm[:])
        else:
            for i in range(num):
                if chosen[i]:
                    continue
                chosen[i] = True
                prm.append(i)
                search()
                chosen[i] = False
                prm.pop()

    search()
    return result


if __name__ == '__main__':
    prms = permutations(9)
    print(len(prms))
    for p in prms:
        print(p)
