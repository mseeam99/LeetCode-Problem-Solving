class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for i in range(len(strs)):
            tempString = ''.join(sorted(strs[i]))
            if tempString not in hashMap.keys():
                hashMap[tempString] = [strs[i]]
            else:
                hashMap[tempString].append(strs[i])
        return hashMap.values()

        