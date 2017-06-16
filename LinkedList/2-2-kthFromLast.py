from LinkedList import LinkedList


# Time: O(n)
def kth_to_last(linked_list, k):
    slow = fast = linked_list.head
    for i in range(k):
        if fast is None:
            return None
        fast = fast.nextNode

    while fast:
        slow = slow.nextNode
        fast = fast.nextNode
    return slow.data

linked_list = LinkedList()
linked_list.__generate__(10,0,9)
linked_list.__print__()
print(kth_to_last(linked_list,3))