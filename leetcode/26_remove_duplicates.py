'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.'''

def removeDuplicates(nums) -> int:
    dict = {};
    size = 0;
    counter = 0;
    while counter< len(nums)-size:
        num = nums[counter];
        if num in dict:
            nums.remove(num);
            nums.append(num);
            size+=1;
        else: 
            dict[num] = True;
            counter+=1;


    return len(nums) - size;



def removeDuplicatesOptimized(nums)->int:
    # here we dont care about swapping the duplicate element to the end , we are just pushing unique element to the left
    j = 1 ;
    for i in range(1, len(nums)):
        if(nums[i]!= nums[i-1]):
            nums[j]= nums[i];
            j+=1;

    return j;


myList = [0,0,1,1,1,2,3];
value = removeDuplicatesOptimized(myList);
print(value)
