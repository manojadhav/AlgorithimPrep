def bubbleSort (array):
    issorted = False
    while not issorted:
        issorted = True
        for i in range(len(array) - 1):
            if array[i] > array [i +1]:
                swap (i, i+1 , array)
                issorted = False #cause for bubble sort last iteration shouldn't change any positions in the array
    return array
def swap (i, j, array):
    array [i], array[j] = array[j], array[i]


