class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        vector<int> data;
        ListNode *ans = head, *copy = head;
        while(head){
            data.push_back(head->val);
            head = head->next;
        }
        for(int i = data.size() - 1; i >= 0; i--){
            copy->val = data[i];
            copy = copy->next;
        }
        return ans;
    }
};
