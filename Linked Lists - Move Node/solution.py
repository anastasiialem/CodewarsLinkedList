"""Module move node"""
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
        self.source = source
        self.dest = dest
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

def move_node(source, dest):
    """
    Move node from one list to another
    :param source: list from
    :param dest: list to
    >>> val=move_node(push(Node(1), 2),\
push(Node(2), 7))
    >>> val.source.data
    1
    >>> val.dest.data
    2
    >>> val.dest.next.data
    7
    >>> val1=move_node(push(Node(1), 2),None)
    >>> val1.source.data
    1
    """
    if source is None:
        raise ValueError("List source is empty")
    node=Node(source.data)
    new_node=source.next
    node.next=dest
    return Context(new_node,node)

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
