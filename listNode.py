class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(node: ListNode):
    while node:
        print("{} -> ".format(node.val), end="")
        node = node.next
    print("None")

# pre: x >= 0
def createNum(x: int) -> ListNode:
    root = node = ListNode(0)
    if x == 0:
        return root
    digit = x % 10
    isZero = True if digit == 0 else False # digit must be nonzero
    while digit or isZero:
        isZero = False
        new_node = ListNode(digit)
        node.next = new_node
        node = new_node
        x = x // 10
        digit = x % 10
        if x > 0 and digit == 0:
            isZero = True
    return root.next
