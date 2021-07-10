/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(), *tail;
        int sum, remain, carry = 0;
        // there is at least one node in the linked list, so l1 l2 is not nullptr
        sum = l1->val + l2->val;
        l1 = l1->next;
        l2 = l2->next;
        remain = sum % 10;
        carry  = sum / 10;
        head->val = remain;
        tail = head;
        while(l1 || l2){
            sum = 0;
            if(l1){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2){
                sum += l2->val;
                l2 = l2->next;
            }
            sum += carry;
            remain = sum % 10;
            carry  = sum / 10;
            tail->next = new ListNode(remain);
            tail = tail->next;
        }
        
        if(carry)
            tail->next = new ListNode(carry);
        return head;
    }
};
