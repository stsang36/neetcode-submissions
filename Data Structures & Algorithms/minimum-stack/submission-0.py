class MinStack:

    def __init__(self):
        self.data = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        self.data.append(val)
        
        if self.minstack:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        else:
            self.minstack.append(val)

    def pop(self) -> None:

        if not self.data:
            return

        val = self.data.pop()

        if self.minstack:
            if self.minstack[-1] == val:
                self.minstack.pop()


    def top(self) -> int:
        if not self.data:
            return -1
        
        return self.data[-1]

    def getMin(self) -> int:
        if not self.minstack:
            return -1

        return self.minstack[-1]
        
