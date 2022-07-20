class Solution(object):    
    def ispalindrome(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        
        l, r=0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True
    print(ispalindrome([1,2,2,1]))


#BETTER TIME/SPACE
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def ispalindrome( self,head):
        fast = head
        slow = head

        #find middle (slow pointer)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        #check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    print(ispalindrome([1,2,2,1]))

