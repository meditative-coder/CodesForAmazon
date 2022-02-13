class Stack:
    def __init__(self):
        self.stack = list()
        self.min_elem = -1

    def pop(self):
        if len(self.stack)==0:
            return -1
        if self.top() >= self.min_elem:
            self.stack = self.stack[:-1]
        elif self.top() < self.min_elem:
            self.min_elem = 2 * self.min_elem - self.top()
            self.stack = self.stack[:-1]


    def top(self):
        if len(self.stack)==0:
            return -1
        
        if self.stack[-1] >= self.min_elem:
            return self.stack[-1]
        return self.min_elem

    def push(self, item):
        if len(self.stack) == 0:
            self.stack.append(item)
            self.min_elem = item
        else:            
            if item < self.min_elem:
                newitem = 2*item - self.min_elem
                self.min_elem = item
                self.stack.append(newitem)
            else:
                self.stack.append(item)
    
    def getMin(self):        
        return self.min_elem

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    print(s.getMin())
    s.push(3)
    print(s.getMin())
    s.pop()
    print(s.top())