class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= max_candy)

        return result
if __name__ == "__main__":
    # Example usage
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    sol = Solution()
    result = sol.kidsWithCandies(candies, extraCandies)
    print("Result:", result)