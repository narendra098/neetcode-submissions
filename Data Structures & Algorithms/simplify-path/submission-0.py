class Solution:
    def simplifyPath(self, path: str) -> str:
        p_list = path.split('/')
        stack = []
        for _ in p_list:
            if _ == '' or _ == '.':
                continue
            elif _ == '..':
                if stack: 
                    stack.pop()
            else:
                stack.append(_)
        return '/' + '/'.join(stack)
        