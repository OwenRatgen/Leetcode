class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Make current node point at previous node
        # 2. Iterate to next node

        newHead = None
        currNode = head

        while currNode != None:
            nextNode = currNode.next
            currNode.next = newHead
            newHead = currNode
            currNode = nextNode

        return newHead