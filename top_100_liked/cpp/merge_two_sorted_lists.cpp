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
#define MAX_VALUE 100
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr)
            return l2;
        if(l2 == nullptr)
            return l1;
        int val1, val2;
        ListNode dummy;
        ListNode *head = &dummy, *tail = &dummy; 
        
        while(l1 || l2){
            val1 = (l1 == nullptr) ? MAX_VALUE + 1 : l1->val;
            val2 = (l2 == nullptr) ? MAX_VALUE + 1 : l2->val;
            if(val1 <= val2){
                tail->next = l1;
                l1 = l1->next;
            }
            else{
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }
        return head->next;
    }
};
