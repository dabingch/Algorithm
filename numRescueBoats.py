class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people or limit <= 0: return 0

        people.sort()
        
        left, right = 0, len(people) - 1
        boat = 0

        while left <= right:
            if (people[left] + people[right]) <= limit:
                left += 1
                right -= 1
            else:
                right -= 1

            boat += 1
        
        return boat