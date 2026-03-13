import calendar 
class Solution:
    def dayOfYear(self, date: str) -> int:
        hashMap = {
            "01": 0,
            "02": 31,
            "03": 59,
            "04": 90,
            "05": 120,
            "06": 151,
            "07": 181,
            "08": 212,
            "09": 243,
            "10": 273,
            "11": 304,
            "12": 334
        }
        year, month, day = date.split("-")
        totalDays = hashMap[month] + int(day)
        if calendar.isleap(int(year)) and int(month) > 2:
            totalDays += 1
        return totalDays