from LinkedList import LinkedList


def removeDuplicates(linkedList):
    if linkedList.head is None:
        return
    current = linkedList.head
    seen = set([current.data])
    while current.nextNode:
        if current.nextNode.data in seen:
            current.nextNode = current.nextNode.nextNode
        else:
            seen.add(current.nextNode.data)
            current = current.nextNode
    return linkedList

linkedList = LinkedList()
linkedList.__generate__(20,0,9)
linkedList.__print__()
removeDuplicates(linkedList)
linkedList.__print__()