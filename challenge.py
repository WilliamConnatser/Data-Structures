'''
Find the Smallest Missing Element from a Sorted Array
Given a sorted array of distinct non-negative integers, find the smallest missing element in it.

Examples
Input: A = [0, 1, 2, 6, 9, 11, 15] Output: The smallest missing element is 3

Input: A = [1, 2, 3, 4, 6, 9, 11, 15] Output: The smallest missing element is 0

Input: A = [0, 1, 2, 3, 4, 5, 6] Output: The smallest missing element is 7
'''


'''
Merge M Sorted Lists of Variable Length
Given M sorted lists of variable length, print them out in sorted order efficiently.

Examples
Input: Four sorted lists of variable length

[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]

Output: 10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 40, 48, 93
'''
def merge_arrays(*args):
    if not args:
        return None
    elif len(args) <= 1:
        return args[0]
    
    new_array = []
    for arg in args:
        new_array = merge(new_array, arg)

    return new_array

#Merge Sort Helper
def merge( left, right ):
    # Make empty list to store the result
    result = []
    # While both lists have at least one item
    while len(left) and len(right):
        if left[0] < right[0]:
            # If the first item on the left is smaller than the first on the right
            # Then append it to the result and remove it from the left
            result.append(left[0])
            left = left[1:]
        else:
            # Else the first item on the right is smaller than the first on the left
            # So append it to the result and remove it from the right
            result.append(right[0])
            right = right[1:]

    # If there is 1 item left in the left or right
    # Then append their values to the result
    return  result + left + right


print(merge_arrays([10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]))
print(merge_arrays([10, 20, 30, 40]))