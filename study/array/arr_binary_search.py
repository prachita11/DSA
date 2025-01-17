'''Binary search is a type of searching algoirthm where each array is divided into two parts ,
if the last value is less than the value desired the second part is used for searching and is further divided into parts till the 
desired outcome is found 
- Time complexity O(logn)
- works on  sorted array
'''

# Assuming this is sorted by ascending order
n=4;
test_set=[3,4,5,6]

def binary_search(n,arr):
    print("array "+' '.join([str(s) for s in arr]))
    if(len(arr)==1):
        if(arr[0] == n):
            print ('Value found');
            return;
        else:
            print('Value not found');
            return;

    else:
        middle = int(len(arr)/2);
        print("middle "+str(middle))
        if(arr[middle] == n):
            print('Value found');
        elif arr[middle] > n:
            binary_search(n,arr[middle + 1: len(arr)]);
        else:
            binary_search(n,arr[0: middle]);



binary_search(n,test_set);
        




