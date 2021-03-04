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

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    root = node = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        val1 = val2 = 0
        if l1:
            val1 = l1.val
            l1 = l1.next
        if l2:
            val2 = l2.val
            l2 = l2.next
        carry, newVal = divmod(val1 + val2 + carry, 10)
        newNode = ListNode(newVal)
        node.next = newNode
        node = newNode
    return root.next

l1 = createNum(9999)
l2 = createNum(9999999)
result = addTwoNumbers(l1, l2)
printList(result)
