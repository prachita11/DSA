def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False;
    sValue={};
    tValue={};

    for i  in s:
        sValue[i] = sValue[i] +1 if i in sValue  else 0;
    for j in t:
        if j not in sValue:
            return False;
        tValue[j] = tValue[j] +1 if j in tValue  else 0;
    
    return sValue ==tValue;
        
 

output = isAnagram('sabced','ecbasf');
print(output)
       
        