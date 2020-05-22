from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        
        if not s or len(s) == 1:
            return s
        
        freq_dict = defaultdict(int)
        out = []
        
        for i in s:
            freq_dict[i] += 1            
        
        for ch, freq in sorted(freq_dict.items(), key = lambda x:x[1], reverse=True):
            out.append(ch*freq)
            
        return ''.join(out)