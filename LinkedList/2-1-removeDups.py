from LinkedList import LinkedList

# Time : O(n)
# Space: O(n)
def remove_duplicates(linked_list):
    if linked_list.head is None:
        return
    current = linked_list.head
    seen = set([current.data])
    while current.nextNode:
        if current.nextNode.data in seen:
            current.nextNode = current.nextNode.nextNode
        else:
            seen.add(current.nextNode.data)
            current = current.nextNode
    return linked_list

# Time: O(n)
def remove_duplicates_without_buffer(linked_list):
    if linked_list.head is None:
        return
    current = linked_list.head
    while current:
        runner = current
        while (runner.nextNode):
            if current.data == runner.nextNode.data:
                runner.nextNode = runner.nextNode.nextNode
            else:
                runner = runner.nextNode
        current = current.nextNode
    return linkedList


linkedList = LinkedList()
linkedList.__generate__(20,0,9)
linkedList.__print__()
remove_duplicates_without_buffer(linkedList)
linkedList.__print__()