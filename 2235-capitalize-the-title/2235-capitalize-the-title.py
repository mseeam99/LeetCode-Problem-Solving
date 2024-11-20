class Solution:
    def capitalizeTitle(self, title: str) -> str:

        array = title.split(" ")

        for i in range(len(array)):
            if len(array[i]) != 1 and len(array[i]) != 2:
                array[i] = array[i].lower()
                string = array[i]
                firstChar = ""
                firstChar += string[0].upper()
                firstChar += string[1:]
                array[i] = firstChar
            else:
                array[i] = array[i].lower()
            
        return " ".join(array)
        
        