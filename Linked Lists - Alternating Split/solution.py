"""Module spliting"""
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

class Context:
    """
    class Context
    """
    def __init__(self, source, dest):
        """
        Function init
        :param self: self param
        :param source: start
        :param dest: end
        """
        self.first = source
        self.second = dest

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

def alternating_split(head):
    """
    Function alternating_split
    :param head: head to start
    >>> n1=push(Node(5), 6)
    >>> n2=push(n1,3)
    >>> n3=push(n2,1)
    >>> val1=alternating_split(push(n3, 2))
    >>> val1.first.data
    2
    >>> val1.first.next.data
    3
    >>> val1.first.next.next.data
    5
    >>> val1.second.data
    1
    >>> val1.second.next.next is None
    True
    """
    if head is None or head.next is None:
        raise ValueError("should be list of length 2+")
    head1=head
    node1=head1
    head2=head.next
    node2=head2
    node=head.next
    while node is not None and node.next is not None:
        node1.next=node.next
        if node.next.next is not None:
            node2.next=node.next.next
            node2=node2.next
        node=node.next
        node1=node1.next
    node1.next=None
    node2.next=None
    return Context(head1,head2)

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
