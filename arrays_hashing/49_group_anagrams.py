from typing import List, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_map = defaultdict(list)
        for s in strs:
            map_key = [0]*26
            for char in s:
                map_key[ord(char)-97] += 1
            
            freq_map[tuple(map_key)].append(s)
        
        return list(freq_map.values())
        