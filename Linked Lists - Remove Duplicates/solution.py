"""Module for removing duplicates"""
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

def remove_duplicates(head):
    """
    Removes duplicates
    :param head: heaf to start
    >>> val=remove_duplicates(push(Node(1), 1))
    >>> val.data
    1
    >>> val.next is None
    True
    >>> n1=push(Node(5), 5)
    >>> n2=push(n1,2)
    >>> n3=push(n2,2)
    >>> val1=remove_duplicates(push(n3, 1))
    >>> val1.data
    1
    >>> val1.next.data
    2
    >>> val1.next.next.data
    5
    >>> val1.next.next.next is None
    True
    """
    if head is None:
        return None
    node=head
    while node.next is not None:
        if node.data==node.next.data:
            node.next=node.next.next
        else:
            node=node.next
    return head

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
