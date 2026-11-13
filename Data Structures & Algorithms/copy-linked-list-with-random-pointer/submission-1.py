class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        clones = {None: None}
        
        curr = head
        while curr:
            copy_node = Node(curr.val)
            clones[curr] = copy_node
            curr = curr.next
            
        curr = head
        while curr:
            copy_node = clones[curr] 
            copy_node.next = clones[curr.next]
            copy_node.random = clones[curr.random]
            curr = curr.next
            
        return clones[head]