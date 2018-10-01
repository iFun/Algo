/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */


// loop each linkedlist to the end, if not the same then return null
// loop longer linkedlist first til they are the same and loop both linkedlist together
var getIntersectionNode = function (headA, headB) {
  if (!headA || !headB) {
    return null
  }

  if (headA.next === null && headB.next === null) {
    if (headA === headB) {
      return headA
    } else {
      return null
    }
  }

  var lengthA = 1;
  var lengthB = 1;
  var curA = headA;
  var curB = headB;


  while (curA.next !== null) {
    curA = curA.next
    lengthA++
  }

  while (curB.next !== null) {
    curB = curB.next
    lengthB++
  }

  if (curA !== curB) {
    return null
  }
  var longer;
  var diff;
  var shorter;

  if (lengthA > lengthB) {
    longer = headA
    shorter = headB
    diff = lengthA - lengthB
  } else {
    longer = headB
    shorter = headA
    diff = lengthB - lengthA
  }

  while (diff !== 0) {
    diff--
    longer = longer.next
  }

  while (longer !== shorter) {
    longer = longer.next
    shorter = shorter.next
  }

  return longer


};
