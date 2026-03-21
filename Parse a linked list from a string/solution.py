"""Module from string to list"""
class Node:
    """
    class Node
    """
    def __init__(self, data, nextt=None):
        """
        Function __init__
        :param self: self param
        :param data: value
        :param next: next node
        """
        self.data = data
        self.next = nextt
def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Fuction from string to linked list
    :param list_repr: string from
    >>> val=linked_list_from_string('1 -> 2 -> 3 -> None')
    >>> isinstance(val,Node)
    True
    >>> val.data
    1
    >>> val.next.data
    2
    >>> val.next.next.next is None
    True
    >>> linked_list_from_string('None') is None
    True
    """
    lst=list_repr.split(' -> ')
    if len(lst)<2:
        return None
    node=Node(int(lst[0]))
    probe=node
    lenght=len(lst)
    for i in range(1,lenght-1):
        probe.next=Node(int(lst[i]))
        probe=probe.next
    probe.next=None
    return node

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
