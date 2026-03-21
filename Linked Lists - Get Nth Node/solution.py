"""Module get nth node"""
class Node:
    """
    class Node
    """
    def __init__(self, data,nextt = None):
        """
        Function init 
        :param self: self param
        :param data: value
        :param next: next node
        """
        self.data = data
        self.next = nextt

def get_nth(node, index):
    """
    Function return node on index
    :param node: linked list
    :param index: index to find node in
    >>> linked_list = Node(1, Node(2, Node(3, None)))
    >>> get_nth(linked_list, 0).data
    1
    >>> get_nth(linked_list, 1).data
    2
    >>> get_nth(linked_list, 2).data
    3
    """
    if node is None:
        raise ValueError("None linked list")
    if index<0:
        raise IndexError("Invalid index value")
    idx=0
    while idx!=index:
        if node is None or node.next is None:
            raise IndexError("Invalid index value")
        node=node.next
        idx+=1
    return node

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
