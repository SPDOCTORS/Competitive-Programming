class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st=[]
        for cur in asteroids:
            alive=True
            while st and st[-1]>0 and cur<0:
                if abs(st[-1])<abs(cur):
                    st.pop()
                elif abs(st[-1])>abs(cur):
                    alive=False
                    break
                else:
                    st.pop()
                    alive=False
                    break
            if alive:
                st.append(cur)
        return st

        