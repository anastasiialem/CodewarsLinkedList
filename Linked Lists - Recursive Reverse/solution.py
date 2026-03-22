"""Module recursive reverse of linked list"""
class Node:
    """
    class Node
    """
    def __init__(self, data=None):
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

def reverse(head):
    """
    Recursive reverse linked list
    :param head: head to start
    >>> val=reverse(push(Node(3), 1))
    >>> val.data
    3
    >>> val.next.data
    1
    >>> val.next.next is None
    True
    >>> n1=push(Node(5), 6)
    >>> n2=push(n1,3)
    >>> n3=push(n2,1)
    >>> val1=reverse(push(n3, 2))
    >>> val1.data
    5
    >>> val1.next.data
    6
    >>> val1.next.next.data
    3
    """
    if head is None:
        return None
    if head.next is None:
        return head
    node=reverse(head.next)
    head.next.next = head
    head.next = None
    return node

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
