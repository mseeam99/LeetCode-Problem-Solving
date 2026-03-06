class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToRating_HashMap = {}
        self.cuisineToHeap = defaultdict(SortedList)
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.foodToRating_HashMap[food] = (rating,cuisine)
            self.cuisineToHeap[cuisine].add((-rating,food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.foodToRating_HashMap[food]
        self.foodToRating_HashMap[food] = [newRating,cuisine]
        self.cuisineToHeap[cuisine].remove((-rating, food))
        self.cuisineToHeap[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineToHeap[cuisine][0][1]
        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)