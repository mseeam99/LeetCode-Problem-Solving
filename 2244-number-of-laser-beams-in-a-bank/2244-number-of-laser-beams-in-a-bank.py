class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        count           = 0
        lastCount       = 0

        for i in range(len(bank)):
            robotCount = bank[i].count("1")
            if robotCount == 0:
                continue
            else:
                count += robotCount * lastCount
                lastCount = robotCount
                
        return count


        

        