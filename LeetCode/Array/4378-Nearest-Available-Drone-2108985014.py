class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ans=-1
        mini=float('inf')
        for i in range(len(drones)):
            x,y,z=drones[i]
            tx,ty=target
            distance=abs(x-tx)+abs(y-ty)
            if distance<=z:
                if distance<mini:
                    mini=distance
                    ans=i
        return ans        