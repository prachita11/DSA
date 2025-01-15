'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?'''

''' Solution :
Brute force - two loops , add and compare. '''

def two_sum(arr, sum):
    sum_arr=[];
    for  i in range(len(arr)):
        if(i>=sum):
            continue;
        if(i== len(arr-1)):
            break;
        for j in range(i+1, len(arr)):
            if(j>=sum):
                continue;
            if(arr[i]+arr[j] == sum):
                sum_arr.append(i);
                sum_arr.append(j);
        

        print(" index:"+ str(i)+" value"+ str(arr[i]))
    return sum_arr;


def two_sum_optimized(arr, sum):
    sum_arr=[];
    value_dic={};
    for  i in range(len(arr)):
        if(i == 0):
            value_dic[str(arr[i])] = i;
            continue;
        
        else:
            diff = sum - arr[i];
            if str(diff) in value_dic:
                sum_arr.append(i);
                sum_arr.append(value_dic[str(diff)]);
                break;
            else:
                value_dic[str(arr[i])]= i;
        
        

        print(" index:"+ str(i)+" value"+ str(arr[i]))
    return sum_arr;


value =[-3,4,3,90]
target = 0;
result = two_sum_optimized(value,target);
print(*result, sep =', ')