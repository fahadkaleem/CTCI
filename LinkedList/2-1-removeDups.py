import LinkedList


def removeDuplicates(linkedList):
    if linkedList.head is None:
        return 0
    else:
        current = linkedList.head
        seen = set[current.value]
        while (current):
            if current.value in seen:
                current.nextNode = current.nextNode.nextNode
            else:
                seen.add(current.value)
                current = current.value
    return linkedList

linkedList = LinkedList()
linkedList.__generate__(20,0,9)
linkedList.__print__()
removeDuplicates(linkedList)
linkedList.__print__()