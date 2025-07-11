class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        maxLength = 1
        pointer = 0

        while pointer < len(arr) - 1:
            currentLength = 1
            for i in range(pointer + 1, len(arr)):
                if arr[i] > arr[i - 1]:
                    sign = ">"
                elif arr[i] < arr[i - 1]:
                    sign = "<"
                else:
                    break  # equal elements break turbulence

                if i == pointer + 1:
                    currentLength += 1
                else:
                    if (arr[i - 1] > arr[i - 2] and arr[i] < arr[i - 1]) or \
                       (arr[i - 1] < arr[i - 2] and arr[i] > arr[i - 1]):
                        currentLength += 1
                    else:
                        break

            maxLength = max(maxLength, currentLength)
            pointer += max(1, currentLength - 1)

        return maxLength
