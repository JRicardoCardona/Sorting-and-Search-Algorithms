
# Sorted number array (Non decreasing)
numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


def binarySearch_while(numbers, look_num):

    low = 0
    high =  len(numbers)-1

    # the array must at least have one number
    while low <=high:

        midIndex = (high+low)//2
        mid_num = numbers[midIndex]

        if look_num == mid_num:
            return midIndex
        
        elif look_num<mid_num:
            high = midIndex-1

        else:
            low = midIndex+1

    return -1


def binary_search_recursive(numbers, look_num, low=0, high=None):

    if high == None:
        high = len(numbers)-1

    if low > high:
        return -1

    midIndex = (high+low)//2
    midnum = numbers[midIndex]

    if look_num == midnum:
        return midIndex

    elif look_num < midnum:
        return binary_search_recursive(numbers, look_num, low, high=midIndex-1)

    else:
        return binary_search_recursive(numbers, look_num, midIndex+1, high)

    
# Test the functions
look_num = 9
print(binarySearch_while(numbers, look_num))
print(binary_search_recursive(numbers, look_num))

look_num = 30
print(binarySearch_while(numbers, look_num))
print(binary_search_recursive(numbers, look_num))

look_num = 1
print(binarySearch_while(numbers, look_num))
print(binary_search_recursive(numbers, look_num))

look_num = 100
print(binarySearch_while(numbers, look_num))
print(binary_search_recursive(numbers, look_num))

