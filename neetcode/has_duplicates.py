def hasDuplicate(nums) -> bool:
    counter = {};
    for i in nums:
        if i in counter:
            return True;
        counter[i] = 1;

    return False;


arr=[1,2,3,4];
output = hasDuplicate(arr);
print(output)
         