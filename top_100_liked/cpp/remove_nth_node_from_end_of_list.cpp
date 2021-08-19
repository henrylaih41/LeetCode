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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fast = head, *slow = head;
        int count = 0;
        // walk n steps ahead
        // |-> slow    |->fast 
        // o o o ... o o
        //   | n nodes |
        //  _ _ ..... _  n links
        for(int i = 0; i < n; i++)
            fast = fast->next;
        while(fast && fast->next != nullptr){
            fast = fast->next;
            slow = slow->next;
        }
        // slow.next is the one we want to remove, it would never be nullptr
        // fast might be null, handle this edge case
        if(fast == nullptr)
            head = head->next;
        else{
            slow->next = slow->next->next;
        }
        
        return head;
    }
};
