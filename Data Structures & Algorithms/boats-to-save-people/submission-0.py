class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        # 1, 2, 4, 5 
        # l        r
        # if l + r == limit: l++, r--
        # if l + r > limit: if l > r: l ++ else: r--
        # if l + r < limit: l++, r--
        # 1, 2, 2, 3, 3
        #    lr
        boats = 0
        while l <= r:
            if l != r and people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1 
            boats += 1
        return boats
        
        