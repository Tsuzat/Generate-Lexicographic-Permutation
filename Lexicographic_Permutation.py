def Generate_Lexicographic_Permutation(s:list):

    k = len(s)-2 
    
    # getting value of k for which, s[k]<s[k+1]
    while not (k<0 or s[k]<s[k+1]):
        k -= 1
    
    #if no such k then it's last permutation 
    if k<0:
        return False
    
    #else:
    
    # getting I such that s[k]<s[I]
    I = len(s)-1
    
    while not(s[I]>s[k]):
        I -= 1
    
    #sawping s[k] and s[I]
    s[I],s[k] = s[k],s[I]
    
    # reversing s[k+1:]
    s[k+1:] = reversed(s[k+1:])
    
    return True
