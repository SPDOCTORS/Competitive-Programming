class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        i = 0
        while i < len(asteroids) - 1:
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if abs(asteroids[i])>abs(asteroids[i+1]):
                    asteroids.pop(i+1)
                elif abs(asteroids[i])<abs(asteroids[i+1]):
                    asteroids.pop(i)
                    i=max(0,i-1)
                else:
                    asteroids.pop(i+1)
                    asteroids.pop(i)
                    i=max(0,i-1)
            else:
                i+=1
        return asteroids
        