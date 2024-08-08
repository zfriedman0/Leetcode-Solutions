class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    values1 = [node.val for node in list1]
    values2 = [node.val for node in list2]

    merged = sorted(values1 + values2)

    return merged

n1 = ListNode(1, 2)
n2 = ListNode(2, 4)
n3 = ListNode(4)

n4 = ListNode(1, 3)
n5 = ListNode(3, 4)
n6 = ListNode(4)

l1 = [n1, n2, n3]
l2 = [n4, n5, n6]

print(mergeTwoLists(l1, l2))
