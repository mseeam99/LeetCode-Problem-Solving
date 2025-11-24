class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        lastChar = 0
        pointer = 0
        while pointer <= len(bits)-1:
            if bits[pointer] == 1 and (bits[pointer+1] == 0 or bits[pointer+1] == 1):
                lastChar = 1
                pointer += 2
            elif bits[pointer] == 0:
                lastChar = 0
                pointer += 1
        return True if lastChar == 0 else False