# A binary search algorithm splits a list of data in half until it finds the target
# To create this algorithm we will need:

# - a function that takes a list and target parameters
def BinarySearch(list, target):
    # - key variables (start, middle and end)
    middle = 0
    start = 0
    end = len(list)
    steps = 0 

    # - recursion or while loop
    while(start <= end):
        print("Step", steps, ":" ,str(list[start:end+1])) # shows list at that certain step
        
    # - Increase the steps each a split is done
        steps = steps + 1
        middle = (start + end) // 2

        # - conditions to track target position
        if target == list[middle]:
            return middle
        
        if target < list[middle]:
            end = middle - 1 
        else:
            start = middle + 1 # creates new list to do another binary search on
    
    return -1 

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BinarySearch(mylist, 8)