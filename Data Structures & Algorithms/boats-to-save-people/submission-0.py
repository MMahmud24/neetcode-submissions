class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            total = people[l] + people[r]
            if total > limit:
                r-=1
                count+=1
            else:
                l+=1
                r-=1
                count+=1

        return count