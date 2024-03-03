# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def push(self, item):
#         self.items.insert(0,item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print("Error: Stack is empty")
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             print("Error: Stack is empty")
#
#     def size(self):
#         return len(self.items)
#
# stack = Stack()
# stack.push(12)
# stack.push(13)
# stack.push(14)
# stack.push(15)
# stack.push(16)
# print(stack.items)
# for i in stack.items:
#     print(i)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
# print(queue.size())
# print(queue.is_empty())
queue.enqueue(4)
print(queue.items)

print("this is stack list")
for i in queue.items[-1::-1]:
    print(i)

print("This is Queue list")
for i in queue.items:
    print(i)

