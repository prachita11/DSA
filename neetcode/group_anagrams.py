'''Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''

def groupAnagrams(strs):
    if len(strs) == 1:
        return [strs];
    groupMap = {};
    arr = [];
    for  i in range(len(strs)):
        sortedVal = ''.join(sorted(strs[i]))
        if i==0: 
            groupMap[sortedVal] = 0;
            arr.append([strs[i]]);
            continue;
        if groupMap.get(sortedVal,-1) > -1:
            arr[groupMap.get(sortedVal,-1)].append(strs[i]);
        else:
            groupMap[sortedVal] = len(groupMap.keys());
            arr.append([strs[i]]);
    return arr;

# Naive approach , will optimize later
a = ["zs","sz","t","att","tta"];
print(groupAnagrams(a));