class MinStack:

    def __init__(self):
        # 存放當前元素
        self.stack = []
        # 存放到目前為止的最小值
        self.min_stack = []

    def push(self, val: int) -> None:
        # 1. 將元素放進去
        self.stack.append(val)

        # 2. 更新 minStack
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 1. 清除 min_stack 的值
        self.min_stack.pop()
        # 2. 回傳 stack 頂端的值
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
           return self.min_stack[-1]
        else:
            return None


        
