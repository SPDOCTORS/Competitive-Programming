class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour=hour%12
        angle_minutes=minutes*6.0
        angle_hour=30*hour+0.5*minutes
        angle=abs(angle_hour-angle_minutes)
        angle_min=min(angle,360-angle)
        return angle_min
        