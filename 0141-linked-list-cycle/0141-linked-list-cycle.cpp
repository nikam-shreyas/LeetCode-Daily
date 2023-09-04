/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include<set>
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL){
            return false;
        }
        ListNode* curr = head;
        unordered_set<ListNode*> s;
        while(curr!=NULL){
            if(s.find(curr)!=s.end()){
                return true;
            }
            s.insert(curr);
            curr = curr->next;
        }
        return false;
    }
};