def is_prime(N):
    d = 2
    while N % d != 0:
        d += 1
    return N == d

def all_divs(N):
    d = 1
    divs = []
    while N + 1 != d:
        if N % d == 0:
            divs.append(d)
        d += 1
    return divs

def big_prive_div(N):
    divs = all_divs(N)
    divs.sort(reverse = True)
    for i in range(len(divs)):
        if is_prime(divs[i]):
            return divs[i]

if __name__ == '__main__':
    print(big_prive_div(22))