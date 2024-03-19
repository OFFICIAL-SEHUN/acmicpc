class Stack:
    def __init__(self):
        self.top = [] #top이라는 리스트 생성

    def __len__(self) -> bool:
        return len(self.top)

    def push(self, item):
        self.top.append(item)


    def pop(self):
        self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()

    #스택이 비어있는 지를 bool값으로 반환
    def isEmpty(self) -> bool:
        return len(self.top) == 0