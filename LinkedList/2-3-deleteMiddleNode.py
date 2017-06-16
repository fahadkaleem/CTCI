from LinkedList import LinkedList


def delete_middle_node(linked_list,middle):
    if linked_list.head is None:
        return
    middle.data = middle.nextNode.data
    middle.nextNode = middle.nextNode.nextNode
    return linked_list

linked_list = LinkedList()
linked_list.insert_multiple([5,6,7,8,9])
middle = linked_list.insert(10)
linked_list.insert_multiple([11,12,13,14])
linked_list.__print__()
delete_middle_node(linked_list,middle)
linked_list.__print__()
