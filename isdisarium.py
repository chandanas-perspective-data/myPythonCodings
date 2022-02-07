def is_disarium(n):
    r = 0
    for i in range(len(str(n))):
        r += int(str(n)[i]) ** (i + 1)
    return r == n


print (is_disarium(518))