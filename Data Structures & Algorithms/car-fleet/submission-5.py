class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s]for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            # how many time unit could let this car arrive target
            stack.append((target-p)/s)

            # merge car if cur car will arrive target earlier than frontend car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)