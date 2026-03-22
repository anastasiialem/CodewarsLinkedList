"""Module swaping"""
class Node:
    """
    class Node
    """
    def __init__(self,nextt=None):
        """
        Function init 
        :param self: self param
        :param data: value
        """
        self.next=nextt

def swap_pairs(head):
    """
    Function swap_pairs
    :param head: head to start
    >>> node1=Node()
    >>> node2=Node(node1)
    >>> node3=Node(node2)
    >>> node4=Node(node3)
    >>> val=swap_pairs(node4)
    >>> node3.next is node4
    True
    >>> node4.next is node1
    True
    >>> node1.next is node2
    True
    """
    if head is None:
        return None
    if head.next is None:
        return head
    res=head.next
    node=head
    prev_node=None
    while node is not None and node.next is not None:
        node1=node
        node2=node.next
        node1.next=node2.next
        node2.next=node1
        if prev_node is not None:
            prev_node.next=node2
        prev_node=node2.next
        node=node2.next.next
    return res

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
