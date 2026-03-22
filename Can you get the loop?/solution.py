"""Module get loop"""
class Node:
    """
    class Node
    """
    def __init__(self, nextt):
        """
        Function init 
        :param self: self param
        :param next: next node
        """
        self.next=nextt
def loop_size(node):
    """
    Function loop_size
    :param node: node to start
    >>> node6=Node(None)
    >>> node5=Node(node6)
    >>> node4=Node(node5)
    >>> node3=Node(node4)
    >>> node2=Node(node3)
    >>> node1=Node(node2)
    >>> node6.next=node2
    >>> loop_size(node1)
    5
    """
    if node is None or node.next is None:
        return 0
    future_node=node.next
    while node!=future_node:
        node=node.next
        future_node=future_node.next.next
    count=0
    future_node=future_node.next
    while node!=future_node:
        count+=1
        future_node=future_node.next
    return count+1

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
