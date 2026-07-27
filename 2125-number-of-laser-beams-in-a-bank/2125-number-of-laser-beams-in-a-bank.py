class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        if len(bank) == 0 or len(bank) == 1:
            return 0

        array = []

        for row in range(len(bank)):
            count = 0
            for col in range(len(bank[row])):
                if bank[row][col] == "1":
                    count += 1
            if count != 0:
                array.append(count)

        print(array)

        if len(array) == 0 or len(array) == 1:
            return 0

      
        totalLaser = 0
        for i in range(1,len(array)):
            
            totalLaser += array[i] * array[i-1]


        return totalLaser
            

                    




        