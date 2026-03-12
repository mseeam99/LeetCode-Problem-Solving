class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:


        numbers.sort()
        for i in range(1,len(numbers)):
            if numbers[i].startswith(numbers[i-1]):           
                return False                   

        return True     