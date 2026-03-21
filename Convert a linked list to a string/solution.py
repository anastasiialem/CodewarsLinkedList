"""Module list to string"""
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
def stringify(node):
    """
    Convert list to string
    :param node: node to start
    >>> stringify(Node(1, Node(2, Node(3))))
    '1 -> 2 -> 3 -> None'
    >>> stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
    '0 -> 1 -> 4 -> 9 -> 16 -> None'
    >>> stringify(None)
    'None'
    """
    tx=''
    while node is not None:
        tx=tx+str(node.data)+' -> '
        node=node.next
    tx=tx+'None'
    return tx
if __name__=='__main__':
    import doctest
    print(doctest.testmod())
