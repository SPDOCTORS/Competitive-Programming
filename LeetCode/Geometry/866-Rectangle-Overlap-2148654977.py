class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x_start = max(rec1[0], rec2[0])
        x_end = min(rec1[2], rec2[2])
        width = x_end - x_start
        y_start = max(rec1[1], rec2[1])
        y_end = min(rec1[3], rec2[3])
        height = y_end - y_start
        if width>0 and height>0:
            return True
        return False
        