class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        mySet = set()
        used = [False]*len(digits)

        def recursion(string):


            if len(string) == 3 and (int(string) % 2 == 0) and string[0] != "0":
                mySet.add(int(string))
                return

            
            for i in range(len(digits)):

                if used[i] == True:
                    continue

                if len(string) == 0 and digits[i] == 0:
                    continue

                # last digit must be even
                if len(string) == 2 and digits[i] % 2 != 0:
                    continue

                used[i] = True
                
                recursion(string + str(digits[i]))

                used[i] = False




        recursion("")
        print(mySet)
        return sorted(list(mySet))



        