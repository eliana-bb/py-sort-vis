#Returns an RGB 3-tuplet on a 1530-hue scale
def hue(number):
    if number >= 0 & number <= 1529:
        j = number%255
        f = number//255
        if f == 0:
            currentcolor = (255, j, 0)
        if f == 1:
            currentcolor = (255-j, 255, 0)
        if f == 2:
            currentcolor = (0, 255, j)
        if f == 3:
            currentcolor = (0, 255-j, 255)
        if f == 4:
            currentcolor = (j, 0, 255)
        if f == 5:
            currentcolor = (255, 0, 255-j)
        return tuple(currentcolor)
    else:
        print("Hue " + str(number) + " out of range [0,1529]!")