class Solution:
    def minDeletions(self, s: str) -> int:
        element_count_hashMap = Counter(s)
        count_frequency = {}
        for key,val in element_count_hashMap.items():
            if val not in count_frequency:
                count_frequency[val] = 1
            else:
                count_frequency[val] += 1
        deletions = 0
        for char,val in element_count_hashMap.items():
            frequency = element_count_hashMap[char]
            while frequency > 0 and count_frequency[frequency] > 1:
                count_frequency[frequency] -= 1
                element_count_hashMap[char] -= 1
                deletions += 1
                frequency -= 1
                if frequency > 0:
                    if frequency in count_frequency:
                        count_frequency[frequency] += 1
                    else:
                        count_frequency[frequency] = 1
                if frequency > 0 and count_frequency[frequency] == 1:
                    break
        return deletions