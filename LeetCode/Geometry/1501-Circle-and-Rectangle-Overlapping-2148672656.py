class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter<=x1:
            closestx=x1
        elif x1<=xCenter<=x2:
            closestx=xCenter
        elif xCenter>x2:
            closestx=x2
        if yCenter < y1:
            closesty = y1
        elif y1 <= yCenter <= y2:
            closesty = yCenter
        elif yCenter > y2:
            closesty = y2
        distance_squared = (closestx - xCenter) ** 2 + (closesty - yCenter) ** 2
        if distance_squared <= radius ** 2:
            return True
        return False
        