"""
using hash function, hash(x) == hash(y), then x == y
Time Complexity = O(N)
Space Complexity = O(N)
"""
def findAnagrams(s, p):
    
        if not s or not p:
            return []
        
        hash_s = sum(hash(i) for i in s[:len(p)])
        hash_p = sum(hash(i) for i in p)
        out = []
        if hash_s == hash_p:
            out.append(0)
            
        for indx, _  in enumerate(zip(s, s[len(p):]), 1):
            out_, in_ = _
            print(_)
            hash_s += hash(in_) - hash(out_)
            if hash_s == hash_p:
                out.append(indx)                 
                
        return out

print(findAnagrams("cbaebabacd", "abc"))