class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # turn data to [[p1, s1], [p2, s2]...]
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        # reversed iterate to iterate from the farthest car to closest car
        for p, s in sorted(pair)[::-1]:
            # append how many time unit should let this car arrive target
            stack.append((target-p)/s)

            # merge car if cur car will arrive target earlier than frontend car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # stack element count will be the car fleet count
        return len(stack)
