

def queens(n):
    cols = [False] * n
    diag1 = [False] * (2*n - 1)
    diag2 = [False] * (2*n - 1)
    cnt = 0

    def search(r):
        nonlocal cnt
        if r == n:
            cnt += 1
        else:
            for c in range(n):
                if cols[c] or diag1[r + c] or diag2[c + n - 1 - r]:
                    continue
                cols[c] = diag1[r + c] = diag2[c + n - 1 - r] = True
                search(r + 1)
                cols[c] = diag1[r + c] = diag2[c + n - 1 - r] = False

    search(0)
    return cnt


if __name__ == '__main__':
    print(queens(8))
