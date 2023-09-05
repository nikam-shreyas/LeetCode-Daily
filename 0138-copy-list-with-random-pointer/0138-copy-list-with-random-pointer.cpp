#include<map>
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        map<Node*, int> orig;
        map<int, Node*> copy;
        Node* copyHead = new Node(0);
        Node* curr = head;
        Node* copyCurr = copyHead;
        int index = 0;
        while(curr!=NULL){
            copyCurr->next = new Node(curr->val);
            orig[curr] = index;
            curr=curr->next;
            copyCurr = copyCurr->next;
            copy[index] = copyCurr;
            index+=1;
        }
        curr = head;
        copyCurr = copyHead->next;
        while(curr!=NULL){
            // cout<<endl<<curr->random;
            // cout<<endl<<listCopy[curr->random];
            if(curr->random!=NULL){
                copyCurr->random = copy[orig[curr->random]];
            }
            copyCurr = copyCurr->next;
            curr = curr->next;
        }
        return copyHead->next;
        // return NULL;
    }
};