'''Linear search is a type of searching algoirthm where each element in the array is traversed linearly till the desired value is found. 
- Time complexity O(n)
- works on both sorted and unsorted array
'''

n=4;
test_set=[3,14,5,6]

def linear_search(n,arr):
    found = False;
    for i in range(len(arr)):
        if arr[i] == n:
            found = True;
            break;
    if found == True:
        print("Element found at index " + str(i));
    else:
        print("Element not found");

linear_search(n,test_set);
        




