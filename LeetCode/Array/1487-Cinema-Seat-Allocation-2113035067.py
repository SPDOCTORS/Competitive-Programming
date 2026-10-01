from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved=defaultdict(set)
        for row,seat in reservedSeats:
            reserved[row].add(seat)
        group=(n-len(reserved))*2
        left={2,3,4,5}
        middle={4,5,6,7}
        right={6,7,8,9}
        for row,seats in reserved.items():
            if left.isdisjoint(seats) and right.isdisjoint(seats):
                group+=2
            elif left.isdisjoint(seats) or right.isdisjoint(seats) or middle.isdisjoint(seats):
                group+=1
        return group



        