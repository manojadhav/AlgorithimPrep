def validatesubsequence (array, suquence):
    seqidx = 0
    arrayidx = o
    while arrayidx < len(array) and seqidx <len(suquence):
            if suquence[seqidx] == array[arrayidx]:
                seqidx += 1
            arrayidx +=1
    return seqidx == len(suquence) 


def validatesubsequence(array, suquence):
    seqidx = 0
    for value in array:
        if len(suquence) == seqidx:
            break
        if suquence[seqidx] == value:
            seqidx += 1
    return seqidx == len(suquence)