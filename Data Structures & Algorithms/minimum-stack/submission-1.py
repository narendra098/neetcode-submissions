class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        last_pushed_ele, last_min = -1, -1
        if self.st:
            ele = self.st[-1]
            last_pushed_ele, last_min = ele.split(",")
            last_min = int(last_min)
        else:
            last_min = val
        min_so_far = min(val, last_min)
        self.st.append(f"{val},{min_so_far}")

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        ele = self.st[-1]
        a, b = ele.split(",")
        return int(a)
        
    def getMin(self) -> int:
        ele = self.st[-1]
        a, b = ele.split(",")
        return int(b)
        
