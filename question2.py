def frequency(array):
    frequencies = []


    for x in array:
        if x not in frequencies:
            frequencies.append(x)
            count = array.count(x)
            print("frequency of",x," is",count)


array = [1, 2, 3, 4, 1, 2, 2, 3, 4, 4, 5,6,89,80]
frequency(array)
