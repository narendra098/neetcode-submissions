class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for char in s:
            if char != ']':
                st.append(char)
            else:
                substr = ''
                while st[-1] != '[':
                    substr = st.pop() + substr
                st.pop()
                num = ''
                while st and st[-1].isdigit():
                    num = st.pop() + num
                
                st.append(int(num) * substr)
            
        return ''.join(st)
                



       
        