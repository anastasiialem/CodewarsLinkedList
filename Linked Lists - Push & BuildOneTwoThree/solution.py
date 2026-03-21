"""Module push and build"""
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

def build_one_two_three():
    """
    Fuction build_one_two_three
    >>> build_one_two_three().data
    1
    >>> build_one_two_three().next.data
    2
    >>> build_one_two_three().next.next.next is None
    True
    """
    head=None
    for i in range(3,0,-1):
        node=push(head,i)
        head=node
    return node

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
