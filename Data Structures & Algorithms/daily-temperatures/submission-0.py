class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and st[-1][0] < temperatures[i]:
                temp, idx = st.pop()
                ans[idx] = i - idx 
            st.append([temperatures[i], i])
        return ans

        