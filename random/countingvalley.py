def countingValleys(n, s):
    L = 0
    V = 0
    for S in s:
        if S == 'U':
            L += 1
            if L == 0:
                V += 1
        else:
            L -= 1

    # if(finalScore < 0 and finalScoreOld >= 0):
    #     numberOfChanges += 1
    # elif(finalScore > 0 and finalScoreOld <= 0):
    #     numberOfChanges += 1
    print(V)


countingValleys(12, 'DDUUDDUDUUUD')
