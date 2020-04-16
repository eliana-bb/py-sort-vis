import imgout
import random

arrayLength = 256

## Standard Scripts ##

def createShuffledArray(length):
    array = []
    for i in range(length):
        array.append(i)

    for j in range(length-1, 0, -1):
        r = random.randint(0,j+1)
        array[r],array[j] = array[j],array[r] 
    
    return array

def isSorted(array):
    for i in range(len(array)-1):
        if array[i] >= array[i+1]:
            return False
        return True

array = createShuffledArray(arrayLength)

## Begin Algorithm ##

if __name__ == '__main__':

    numSorted = 0
    currentPos = 0
    cycles = 0
    multiprocessing.set_start_method('spawn')
    


    while numSorted < arrayLength:
        while currentPos < (arrayLength - numSorted - 1):
            if array[currentPos] > array[currentPos + 1]:
                array[currentPos], array[currentPos + 1] = array[currentPos + 1], array[currentPos]
            imgout.sortImage(array,cycles)
            cycles = cycles + 1
            #print("Cycle "+str(cycles))
            currentPos = currentPos + 1
        currentPos = 0
        numSorted = numSorted + 1

    print("Done!")
    while True: #comment this out to close the python window when done
        pass
