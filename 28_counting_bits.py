
#Brute Force
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        if num == None:
            return num
        
        out = [0]
        
        for i in range(1 , num + 1):
            out.append(list(bin(i)).count('1'))
            
        return out



# O(N) solution
def countbits(N):
    arr = [0]*(N+1)
    
    for i in range(1, N+1):
        arr[i] = arr[i >> 1] + (i & 1)
    
    return arr