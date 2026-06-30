class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        zip and sort the pos and speed
        loop through and calculate the time 
        then check the current time and the ToS
        if its time is less, then skip it because it'll catch up
        otherwise it'll be a part of the fleet
        '''
        stack = []
        pairs = sorted(zip(position, speed), reverse = True)
        for pos, spd in pairs:
            time = (target - pos)/spd
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)