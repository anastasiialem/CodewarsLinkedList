"""Module sorted linked list by insert"""
class Node:
    """
    class Node
    """
    def __init__(self, data):
        """
        Function init 
        :param self: self param
        :param data: value
        """
        self.data = data
        self.next=None

def push(head, data):
    """
    Function push node before head
    :param head: head
    :param data: value
    >>> push(None, 1).data
    1
    >>> push(None, 1).next is None
    True
    >>> push(Node(1), 2).data
    2
    >>> push(Node(1), 2).next.data
    1
    """
    node=Node(data)
    node.next=head
    return node

def sorted_insert(head, data):
    """
    Function insert in sorted list
    :param head: head
    :param data: value to insert
    >>> val=sorted_insert(push(Node(3), 1), 2)
    >>> val.data
    1
    >>> val.next.data
    2
    >>> val=sorted_insert(push(Node(2), 1), 5)
    >>> val.data
    1
    >>> val.next.data
    2
    >>> val.next.next.data
    5
    """
    if head is None:
        return Node(data)
    if data<head.data:
        node=Node(data)
        node.next=head
        return node
    node=head
    while head is not None:
        if head.next is not None and data>head.next.data:
            head=head.next
        else:
            node2=Node(data)
            node2.next=head.next
            head.next=node2
            break
    return node
if __name__=='__main__':
    import doctest
    print(doctest.testmod())
