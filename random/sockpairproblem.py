import math


def sockMerchant(n, ar):
    hashmap = {}
    number_of_pairs = 0
    for socks in ar:
        if(socks in hashmap.keys()):
            hashmap[socks] += 1
        else:
            hashmap[socks] = 1
    for sock in hashmap:
        number_of_pairs += math.floor(hashmap[sock]/2)

    print(number_of_pairs)


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
