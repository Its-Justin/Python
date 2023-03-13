def countdown(number):
    arr=[]
    for x in range(number,-1, -1):
        arr.append(x)
    return(arr)
print(countdown(5))

def print_and_return(arr):
        print(arr[0])
        return(arr[1])
print(print_and_return([1,2]))

def first_plus_length(arr):
    x = arr[0] + len(arr)
    return(x)
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(arr):
    if len(arr) < 2:
        return(False)
    new_arr=[]
    for arr_value in range(len(arr)):
        if arr[arr_value] > arr[1]:
            new_arr.append(arr[arr_value])
    print(len(new_arr))
    return(new_arr)
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(size,value):
    new_arr=[]
    for x in range(size):
        new_arr.append(value)
    return(new_arr)
print(length_and_value(4,7))
print(length_and_value(6,2))