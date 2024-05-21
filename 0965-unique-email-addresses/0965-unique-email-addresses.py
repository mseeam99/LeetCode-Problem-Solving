class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        myList = []
        for i in range(len(emails)):
            each = emails[i]
            if "." in each:
                indexOfAtSign = each.index("@")
                each = each[:indexOfAtSign].replace(".","") + each[indexOfAtSign:]
            if "+" in each:
                indexOfAtSign   = each.index("@")
                indexOfPlusSign = each.index("+")
                each = each[:indexOfPlusSign] + each[indexOfAtSign:]
            if each not in myList:
                myList.append(each)
        return len(myList)