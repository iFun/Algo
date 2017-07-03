/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null){
            return true;
        }
        
        if(head.next.next == null){
            return head.next.val == head.val;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        
        //slow gets to the middle
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        //check if its odd 
        if(fast != null){
            slow = slow.next;
        }
        slow = reverse(slow);
        fast = head;
        
        //reverse the half and check again
        while(slow != null){
            if(slow.val != fast.val){
                return false;
            }
            fast = fast.next;
            slow = slow.next;
        }
        
        return true;
    }

    //reverse the half linkedlist    
    public ListNode reverse(ListNode head){
        ListNode prev = null;
        
        while(head != null){
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
        
    }
}
