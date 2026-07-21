class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:
            if ch != ']':
                st.append(ch)
            else:
                sub = ''
                while st[-1] != '[':
                    sub = st.pop() + sub
                st.pop()
                num = ''
                while st and st[-1].isdigit():
                    num = st.pop() + num
                st.append(int(num)*sub)
        return ''.join(st)