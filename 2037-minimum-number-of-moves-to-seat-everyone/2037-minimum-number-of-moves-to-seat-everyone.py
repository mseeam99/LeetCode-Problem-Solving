class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()


        changedNeeded = 0

        for i in range(len(seats)):
            changedNeeded += abs(seats[i] - students[i])




        return changedNeeded

        