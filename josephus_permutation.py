def who_goes_free(n,k):
    return 0 if n==1 else (who_goes_free(n-1, k) + k) % n



print (who_goes_free(5,3))

print (who_goes_free(9,3))


# solution 2

def who_goes_free(n, k):
    p = 0
    for i in range(1, n + 1):
        p += k
        p %= i
    return p


print (who_goes_free(3,3))