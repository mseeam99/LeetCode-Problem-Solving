class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        leftTime = 1
        rightTime = max(ranks)*cars*cars

        while leftTime < rightTime:
            middleTime = leftTime + (rightTime-leftTime) // 2
            totalCarFixed = 0
            for rank in ranks:
                totalCarFixed += floor(int(middleTime // rank) ** 0.5)
            if totalCarFixed < cars:
                leftTime = middleTime + 1
            elif totalCarFixed >= cars:
                rightTime = middleTime
        return leftTime